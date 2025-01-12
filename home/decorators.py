# your_app/decorators.py
from django.shortcuts import redirect
from functools import wraps

def restrict_access(view_func):
    @wraps(view_func)
    def _wrapped_view_func(request, *args, **kwargs):
        # Check if the user is authenticated or if they have specific session data
        if not request.user.is_authenticated:
            return redirect('index')  # Redirect to the index page or any other page
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func
