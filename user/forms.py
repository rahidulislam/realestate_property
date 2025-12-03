from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make email required and apply bootstrap classes to widgets
        self.fields["email"].required = True
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})

    def save(self, commit=True):
        """Override save to use CustomUser.objects.create_customer()"""
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password1"]
        first_name = self.cleaned_data.get("first_name", "")
        last_name = self.cleaned_data.get("last_name", "")

        user = CustomUser.objects.create_customer(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        return user


class CustomAuthenticationForm(AuthenticationForm):
    """AuthenticationForm that styles fields and uses 'Email' label."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Update widget classes for bootstrap
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})

        # Change label shown for the username field to 'Email'
        if "username" in self.fields:
            self.fields["username"].label = "Email"
