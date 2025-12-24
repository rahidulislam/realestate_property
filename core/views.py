from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView

from user.decorators import seller_required


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


class ContactView(TemplateView):
    template_name = "core/contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class PrivacyPolicyView(TemplateView):
    template_name = "core/privacy_policy.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class TermsView(TemplateView):
    template_name = "core/terms.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class BlogView(TemplateView):
    template_name = "core/blog.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class BlogDetailView(TemplateView):
    template_name = "core/blog_detail.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


@method_decorator([login_required, seller_required], name="dispatch")
class SellerDashboardView(TemplateView):
    template_name = "dashboard/seller/seller_dashboard.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AgentDashboardView(TemplateView):
    template_name = "core/agent_dashboard.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class BuyerDashboardView(TemplateView):
    template_name = "core/buyer_dashboard.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

