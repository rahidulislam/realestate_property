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


class PropertyDetailView(TemplateView):
    template_name = "core/property_detail.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AgentsView(TemplateView):
    template_name = "core/agents.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AgentProfileView(TemplateView):
    template_name = "core/agent_profile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ServicesView(TemplateView):
    template_name = "core/services.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ServiceDetailView(TemplateView):
    template_name = "core/service_detail.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
