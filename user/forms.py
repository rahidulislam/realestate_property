from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "password1", "password2")

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

        user = CustomUser.objects.create_buyer(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        return user

    def clean_email(self):
        email = self.cleaned_data["email"]
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2


class SellerSignupForm(UserCreationForm):
    phone = forms.CharField(max_length=20)
    # company_name = forms.CharField(required=False)
    national_id = forms.CharField(max_length=20)

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name","password1","password2"] + ["phone", "national_id"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control custom-input"
            })

    def save(self, commit=True):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password1"]
        first_name = self.cleaned_data.get("first_name", "")
        last_name = self.cleaned_data.get("last_name", "")

        user = CustomUser.objects.create_seller(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        if commit:
            
            user.sellerprofile.phone = self.cleaned_data["phone"]
            user.sellerprofile.national_id = self.cleaned_data["national_id"]
            user.sellerprofile.save()
            # SellerProfile.objects.create(
            #     user=user,
            #     phone=self.cleaned_data["phone"],
            #     company_name=self.cleaned_data.get("company_name", ""),
            # )
        return user
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2




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
