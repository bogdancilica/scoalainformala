from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from aplicatie2.models import Companies


class CompanyView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/Companies_index.html'


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Companies
    # fields = '__all__'
    fields = ['name', 'company_type', 'website']
    template_name = 'aplicatie2/Companies_form.html'

    def get_success_url(self):
        return reverse('companies:listare')


class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = ['name', 'company_type', 'website']
    template_name = 'aplicatie2/Companies_form.html'

    def get_success_url(self):
        return reverse('companies:listare')

@login_required
def delete_company(request, pk):
    Companies.objects.filter(id=pk).update(active=0)
    return redirect('companies:listare')


@login_required
def activate_company(request, pk):
    Companies.objects.filter(id=pk).update(active=1)
    return redirect('companies:listare')