from django.shortcuts import redirect


def seller_required(view_func):
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != "seller":
            return redirect("user:login")
        if not request.user.sellerprofile.approved:
            return redirect("user:seller_pending")
        return view_func(request, *args, **kwargs)
    return _wrapped