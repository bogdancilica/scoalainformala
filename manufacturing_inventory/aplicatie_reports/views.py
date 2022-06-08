

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.shortcuts import render


from django.urls import reverse
from django.views.generic import ListView, CreateView

from aplicatie_items.models import Items
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


    def form_valid(self, form):
        # if form.is_valid():
        # print(form.cleaned_data['item_no'])
        if form.cleaned_data['quantity'] >= Items.objects.get(item_no=form.cleaned_data['item_no']).quantity:
            errors = form._errors.setdefault('quantity', ErrorList())
            errors.append('Cantitatea este insuficienta!')
            return super(GetItemView, self).form_invalid(form)
        else:
            instance = form.save()
            instance_report = self.model.objects.get(id=instance.id)
            quantity_to_diff = instance_report.quantity
            item_instance = Items.objects.get(id=instance_report.item_no.id)
            initial_quantity = item_instance.quantity
            item_instance.quantity = initial_quantity - quantity_to_diff
            item_instance.save()
        return super(GetItemView, self).form_valid(form)


    def get_success_url(self):
        return reverse('reports:reports_list')


def report_user(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        result = Reports.objects.filter(engineer__username__icontains=searched)
        return render(request, 'aplicatie_reports/search.html', {'searched': searched, 'reports': result})
    else:
        return render(request, 'aplicatie_reports/search.html', {})


def report_project(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        result = Reports.objects.filter(project__project_name__icontains=searched)
        return render(request, 'aplicatie_reports/search1.html', {'searched': searched, 'reports': result})
    else:
        return render(request, 'aplicatie_reports/search1.html', {})
