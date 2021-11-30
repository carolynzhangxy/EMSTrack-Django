import logging
from django.views.generic.base import TemplateView
from rest_framework.authtoken.models import Token
import requests
import os


logger = logging.getLogger(__name__)

class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        SERVER = "UCSD"
        param = {
            'username': os.environ["DASHBOARD_USERNAME_" + SERVER],
            'password': os.environ["DASHBOARD_PASSWORD_" + SERVER],
        }
        url = os.environ["DASHBOARD_AUTHURL_" + SERVER]
        # res = requests.post(url, data=param)
        # res.raise_for_status()
        # token = res.json()['token']
        # token = self.get_token()
        token = url
        # token, _ = Token.objects.get_or_create(user=self.request.user)
        context['token'] = token
        context['user'] = self.request.user

        return context