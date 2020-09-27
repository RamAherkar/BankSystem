from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from django.shortcuts import render



class HomeView(TemplateView):
    template_name = 'core/index.html'



