from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from users.mixins import AdminRequiredMixin


class UserAnalysisView(LoginRequiredMixin, TemplateView):
    template_name = 'user_analysis.html'


class AdminAnalysisView(AdminRequiredMixin, TemplateView):
    template_name = 'admin_analysis.html'
