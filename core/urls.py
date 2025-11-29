from django.urls import path
from .views import HomeView, AboutView, PropertiesView, PropertyDetailView, AgentsView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('properties/', PropertiesView.as_view(), name='properties'),
    path('properties/details/', PropertyDetailView.as_view(), name='property_detail'),
    path('agents/', AgentsView.as_view(), name='agents'),
]