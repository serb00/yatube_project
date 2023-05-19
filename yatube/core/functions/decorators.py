from functools import wraps
from django.shortcuts import redirect


def authorized_only(func):
    @wraps(func)
    def check_user(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect("/auth/login/")
    return check_user


def author_only(func):
    @wraps(func)
    def check_author(request, *args, **kwargs):
        # post_id = kwargs["post_id"]
        if request.user == request.post.author:
            return func(request, *args, **kwargs)
        return redirect(f"/posts/{request.post.pk}/")
    return check_author
