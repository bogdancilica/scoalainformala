from django.urls import path

from aplicatie_userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('new_account/', views.CreateNewAccount.as_view(), name='new_user'),
]