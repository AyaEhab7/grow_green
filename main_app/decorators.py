from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from .models import UserProfile
 
def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role != "admin":
            return HttpResponseForbidden("You do not have permission to access this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def farmer_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role != "farmer":
            return HttpResponseForbidden("You do not have permission to access this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view