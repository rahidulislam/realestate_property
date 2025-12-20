from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import CustomAuthenticationForm, CustomUserCreationForm, SellerSignupForm
from .models import CustomUser


class BuyerSignupView(FormView):
    template_name = "user/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Your buyer account has been created.")
        return super().form_valid(form)


class SellerSignUpView(FormView):
    template_name = "user/seller_signup.html"
    form_class = SellerSignupForm
    success_url = reverse_lazy("user:seller_pending")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Your seller account is pending admin approval.")
        return super().form_valid(form)


class SellerPendingView(TemplateView):
    template_name = "user/seller_pending.html"


class SigninView(LoginView):
    template_name = "user/signin.html"
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("core:home")
    success_message = "You have successfully signed in."

    def get_success_url(self):
        if self.request.user.is_authenticated and self.request.user.role == "buyer":
            return reverse_lazy("core:buyer_dashboard")
        elif self.request.user.is_authenticated and self.request.user.role == "seller":
            return reverse_lazy("core:seller_dashboard")
        elif self.request.user.is_authenticated and self.request.user.role == "agent":
            return reverse_lazy("core:agent_dashboard")
        else:
            return super().get_success_url()

    def form_invalid(self, form):
        email = form.data.get("username")
        if email:
            try:
                user = CustomUser.objects.get(email=email)
                if not user.is_active and user.role == "seller":
                    return redirect("user:seller_pending")
            except CustomUser.DoesNotExist:
                pass
        return super().form_invalid(form)


class SignoutView(LogoutView):
    next_page = reverse_lazy("core:home")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been signed out.")
        return super().dispatch(request, *args, **kwargs)
