from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('items/', views.get_item_list),
    path('items/<int:id>', views.get_specific_item)
]