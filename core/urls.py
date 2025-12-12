from django.urls import path
from .views import (
    HomeView,
    AboutView,
    PropertiesView,
    PropertyDetailView,
    AgentsView,
    AgentProfileView,
    ServicesView,
    ServiceDetailView,
    BlogView,
    BlogDetailView,
    ContactView,
    PrivacyPolicyView,
    TermsView,
    SellerDashboardView,
    AgentDashboardView,
    BuyerDashboardView,
)

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("properties/", PropertiesView.as_view(), name="properties"),
    path("properties/details/", PropertyDetailView.as_view(), name="property_detail"),
    path("agents/", AgentsView.as_view(), name="agents"),
    path("agents/profile/", AgentProfileView.as_view(), name="agent_profile"),
    path("services/", ServicesView.as_view(), name="services"),
    path("services/details/", ServiceDetailView.as_view(), name="service_detail"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("blog/details/", BlogDetailView.as_view(), name="blog_detail"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("privacy-policy/", PrivacyPolicyView.as_view(), name="privacy_policy"),
    path("terms/", TermsView.as_view(), name="terms"),
    path("seller-dashboard/", SellerDashboardView.as_view(), name="seller_dashboard"),
    path("agent-dashboard/", AgentDashboardView.as_view(), name="agent_dashboard"),
    path("buyer-dashboard/", BuyerDashboardView.as_view(), name="buyer_dashboard"),
]
