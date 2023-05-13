from functools import wraps
from django.shortcuts import redirect


def authorized_only(func):
    @wraps(func)
    def check_user(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect("/auth/login/")
    return check_user
