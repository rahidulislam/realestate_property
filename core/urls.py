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
]
