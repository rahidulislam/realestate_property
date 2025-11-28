from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
    template_name = "core/index.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class AboutView(TemplateView):
    template_name = "core/about.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class PropertiesView(TemplateView):
    template_name = "core/properties.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)