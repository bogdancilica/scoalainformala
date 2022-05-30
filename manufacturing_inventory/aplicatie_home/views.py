from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView


class CreateHomeView(LoginRequiredMixin, ListView):
    template_name = 'aplicatie_home/home.html'

    def queryset(self):
        return None
