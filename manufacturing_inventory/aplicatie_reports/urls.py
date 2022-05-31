from django.urls import path
from aplicatie_reports import views

app_name = 'reports'

urlpatterns = [
    path('', views.ReportsView.as_view(), name='reports_list'),
    path('get_item/', views.GetItemView.as_view(), name='get'),
    path('report1/', views.report_user, name='report_by_user'),
    path('report2/', views.report_project, name='report_by_project'),
]