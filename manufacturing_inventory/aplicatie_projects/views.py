from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie_projects.models import Projects


class ProjectsView(LoginRequiredMixin, ListView):
    model = Projects
    template_name = 'aplicatie_projects/projects_index.html'
    paginate_by = 5


class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Projects
    fields = '__all__'
    template_name = 'aplicatie_projects/project_form.html'

    def get_success_url(self):
        return reverse('projects:projects_list')

class EditProjectView(LoginRequiredMixin, UpdateView):
    model = Projects
    fields = '__all__'
    template_name = 'aplicatie_items/item_form.html'

    def get_success_url(self):
        return reverse('projects:projects_list')

@login_required
def delete_project(request, pk):
    Projects.objects.filter(id=pk).update(status=0)
    return redirect('projects:projects_list')

@login_required
def activate_project(request, pk):
    Projects.objects.filter(id=pk).update(status=1)
    return redirect('projects:projects_list')