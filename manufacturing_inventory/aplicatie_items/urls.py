from django.urls import path
from aplicatie_items import views

app_name = 'items'

urlpatterns = [
    path('', views.ItemsView.as_view(), name='items_list'),
    path('add_item/', views.CreateItemView.as_view(), name='add'),
    path('<int:pk>/edit/', views.EditItemView.as_view(), name="edit"),
    path('<int:pk>/delete/', views.delete_item, name='delete'),
    path('<int:pk>/get/', views.GetItemView.as_view(), name="get"),
    path('<int:pk>/activate/', views.activate_item, name='activate'),
    path('inactive_items/', views.ItemsInactiveView.as_view(), name='inactive_items'),
]