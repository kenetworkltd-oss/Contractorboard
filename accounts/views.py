from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ContractorRegistrationForm, HomeownerRegistrationForm
from .models import ContractorProfile, User


def register_contractor(request):
    if request.method == 'POST':
        form = ContractorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = User.CONTRACTOR
            user.save()
            ContractorProfile.objects.create(
                user=user,
                business_name=form.cleaned_data['business_name'],
                niche=form.cleaned_data['niche'],
                service_area=form.cleaned_data['service_area'],
            )
            login(request, user)
            return redirect('dashboard')
    else:
        form = ContractorRegistrationForm()
    return render(request, 'accounts/register_contractor.html', {'form': form})


def register_homeowner(request):
    if request.method == 'POST':
        form = HomeownerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = User.HOMEOWNER
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = HomeownerRegistrationForm()
    return render(request, 'accounts/register_homeowner.html', {'form': form})
