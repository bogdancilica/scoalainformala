from django.urls import path
from aplicatie_home import views

app_name = 'home'

urlpatterns = [
    path('', views.CreateHomeView.as_view(), name='home_page'),
]