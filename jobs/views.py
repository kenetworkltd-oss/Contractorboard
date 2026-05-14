from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from accounts.decorators import homeowner_required
from .models import Job
from .forms import JobForm


def job_list(request):
    jobs = Job.objects.filter(status='open')

    keyword = request.GET.get('q', '')
    niche = request.GET.get('niche', '')
    location = request.GET.get('location', '')
    sort = request.GET.get('sort', 'newest')

    if keyword:
        jobs = jobs.filter(
            Q(title__icontains=keyword) |
            Q(description__icontains=keyword)
        )
    if niche:
        jobs = jobs.filter(niche=niche)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if sort == 'budget_high':
        jobs = jobs.order_by('-budget_max')
    elif sort == 'budget_low':
        jobs = jobs.order_by('budget_min')
    else:
        jobs = jobs.order_by('-created_at')

    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'jobs/job_list.html', {
        'page_obj': page_obj,
        'keyword': keyword,
        'niche': niche,
        'location': location,
        'sort': sort,
        'total_results': paginator.count,
    })


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})


@homeowner_required
def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.homeowner = request.user
            job.save()
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm()
    return render(request, 'jobs/job_create.html', {'form': form})


@login_required
def job_edit(request, pk):
    # Only the homeowner who posted it can edit
    job = get_object_or_404(Job, pk=pk, homeowner=request.user)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/job_edit.html', {'form': form, 'job': job})


@login_required
def job_delete(request, pk):
    # Only the homeowner who posted it can delete
    job = get_object_or_404(Job, pk=pk, homeowner=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'jobs/job_confirm_delete.html', {'job': job})