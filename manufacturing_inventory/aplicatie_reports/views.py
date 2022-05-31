from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView

from aplicatie_reports.models import Reports


class ReportsView(LoginRequiredMixin, ListView):
    model = Reports
    template_name = 'aplicatie_reports/reports_index.html'
    paginate_by = 5


class GetItemView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Reports
    fields = '__all__'
    template_name = 'aplicatie_reports/report_form.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        return reverse('reports:reports_list')


def report_user(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        result = Reports.objects.filter(engineer__icontains=searched)
        return render(request, 'aplicatie_reports/search.html', {'searched': searched, 'reports': result})
    else:
        return render(request, 'aplicatie_reports/search.html', {})


def report_project(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        result = Reports.objects.filter(project__icontains=searched)
        return render(request, 'aplicatie_reports/search1.html', {'searched': searched, 'reports': result})
    else:
        return render(request, 'aplicatie_reports/search1.html', {})
