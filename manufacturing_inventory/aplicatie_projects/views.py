from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie_projects.models import Projects


class ProjectsView(LoginRequiredMixin, ListView):
    model = Projects
    template_name = 'aplicatie_projects/projects_index.html'
    paginate_by = 5


class CreateProjectView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Projects
    fields = '__all__'
    template_name = 'aplicatie_projects/project_form.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        return reverse('projects:projects_list')

class EditProjectView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Projects
    fields = '__all__'
    template_name = 'aplicatie_items/item_form.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        return reverse('projects:projects_list')

@login_required
@permission_required('is_superuser')
def delete_project(request, pk):
    Projects.objects.filter(id=pk).update(status=0)
    return redirect('projects:projects_list')


@login_required
@permission_required('is_superuser')
def activate_project(request, pk):
    Projects.objects.filter(id=pk).update(status=1)
    return redirect('projects:projects_list')