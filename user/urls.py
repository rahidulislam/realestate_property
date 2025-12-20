from django.urls import path
from .views import BuyerSignupView,SellerSignUpView,SellerPendingView, SigninView,SignoutView

app_name = "user"

urlpatterns = [
    path("signup/", BuyerSignupView.as_view(), name="buyer_signup"),
    path("seller-signup/", SellerSignUpView.as_view(), name="seller_signup"),
    path("seller-pending/", SellerPendingView.as_view(), name="seller_pending"),
    path("login/", SigninView.as_view(), name="login"),
    path("logout/", SignoutView.as_view(), name="logout"),
]