from django.urls import path
from .views import BuyerSignupView,SellerSignUpView,SellerPendingView, SigninView,SignoutView, AgentApplicationAplyView, AgentApplicationSuccessView

app_name = "user"

urlpatterns = [
    path("signup/", BuyerSignupView.as_view(), name="buyer_signup"),
    path("seller-signup/", SellerSignUpView.as_view(), name="seller_signup"),
    path("seller-pending/", SellerPendingView.as_view(), name="seller_pending"),
    path("agent-application/", AgentApplicationAplyView.as_view(), name="agent_application_apply"),
    path("agent-application-success/", AgentApplicationSuccessView.as_view(), name="agent_application_success"),
    path("login/", SigninView.as_view(), name="login"),
    path("logout/", SignoutView.as_view(), name="logout"),
]