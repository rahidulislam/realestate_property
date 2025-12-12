from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import CustomAuthenticationForm, CustomUserCreationForm


class SignupView(FormView):
    template_name = "user/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Your buyer account has been created.")
        return super().form_valid(form)


class SigninView(LoginView):
    template_name = "user/signin.html"
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("core:home")
