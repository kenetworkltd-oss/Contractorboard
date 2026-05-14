from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from functools import wraps


def contractor_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_contractor():
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper


def homeowner_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_homeowner():
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper