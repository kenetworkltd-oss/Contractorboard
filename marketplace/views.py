from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Avg
from django.conf import settings
from jobs.models import Job
from accounts.models import ContractorProfile
from .models import Inquiry, Review
from .forms import InquiryForm, ReviewForm


def home(request):
    return render(request, 'marketplace/home.html')


def faq(request):
    return render(request, 'marketplace/faq.html')


def contractor_list(request):
    profiles = ContractorProfile.objects.filter(
        user__is_active=True
    ).annotate(avg_rating=Avg('user__reviews_received__rating'))

    niche = request.GET.get('niche', '')
    location = request.GET.get('location', '')

    if niche:
        profiles = profiles.filter(niche=niche)
    if location:
        profiles = profiles.filter(service_area__icontains=location)

    return render(request, 'marketplace/contractor_list.html', {
        'profiles': profiles,
        'niche': niche,
        'location': location,
    })


def contractor_detail(request, pk):
    profile = get_object_or_404(ContractorProfile, pk=pk)
    reviews = Review.objects.filter(
        contractor=profile.user
    ).order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    can_review = False
    if request.user.is_authenticated and request.user.is_homeowner():
        can_review = not Review.objects.filter(
            contractor=profile.user,
            homeowner=request.user
        ).exists()

    if request.method == 'POST' and can_review:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.contractor = profile.user
            review.homeowner = request.user
            review.save()
            return redirect('contractor_detail', pk=pk)
    else:
        form = ReviewForm()

    return render(request, 'marketplace/contractor_detail.html', {
        'profile': profile,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'can_review': can_review,
        'form': form,
    })


@login_required
def dashboard(request):
    user = request.user
    if user.is_contractor():
        inquiries = Inquiry.objects.filter(
            contractor=user
        ).select_related('job')
        return render(request, 'marketplace/dashboard.html', {
            'inquiries': inquiries,
        })
    else:
        my_jobs = Job.objects.filter(homeowner=user)
        job_ids = my_jobs.values_list('id', flat=True)
        inquiries_received = Inquiry.objects.filter(
            job__in=job_ids
        ).select_related('job', 'contractor')
        return render(request, 'marketplace/dashboard.html', {
            'my_jobs': my_jobs,
            'inquiries_received': inquiries_received,
        })


@login_required
def send_inquiry(request, job_pk):
    job = get_object_or_404(Job, pk=job_pk, status='open')

    if not request.user.is_contractor():
        return redirect('job_detail', pk=job_pk)

    already_sent = Inquiry.objects.filter(
        job=job,
        contractor=request.user
    ).exists()
    if already_sent:
        return redirect('job_detail', pk=job_pk)

    if job.homeowner == request.user:
        return redirect('job_detail', pk=job_pk)

    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.job = job
            inquiry.contractor = request.user
            inquiry.save()
            try:
                send_mail(
                    subject=f'New Inquiry on: {job.title}',
                    message=(
                        f'Hi {job.homeowner.username},\n\n'
                        f'{request.user.username} sent an inquiry on "{job.title}".\n\n'
                        f'Message:\n{inquiry.message}\n\n'
                        f'Login to view and respond.'
                    ),
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[job.homeowner.email],
                    fail_silently=True,
                )
            except Exception:
                pass
            return redirect('job_detail', pk=job_pk)
    else:
        form = InquiryForm()

    return render(request, 'marketplace/inquiry_form.html', {
        'form': form,
        'job': job
    })
    
@login_required
def inquiry_detail(request, pk):
    inquiry = get_object_or_404(Inquiry, pk=pk)
    if request.user != inquiry.job.homeowner and request.user != inquiry.contractor:
        return redirect('dashboard')
    return render(request, 'marketplace/inquiry_detail.html', {'inquiry': inquiry})