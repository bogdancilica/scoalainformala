from django.urls import path
from aplicatie_projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectsView.as_view(), name='projects_list'),
    path('add_project/', views.CreateProjectView.as_view(), name='add'),
    path('<int:pk>/edit/', views.EditProjectView.as_view(), name="edit"),
    path('<int:pk>/delete/', views.delete_project, name='delete'),
    path('<int:pk>/activate/', views.activate_project, name='activate'),

]