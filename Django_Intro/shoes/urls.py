from django.urls import path
from . import views

urlpatterns = [
    path('shoe/list/', views.shoe_list, name='shoe_list'),
    path('shoe/<int:pk>/', views.shoe_detail, name='shoe_detail'),
    path('shoe/create/', views.shoe_create, name='shoe_create'),
    path('shoe/<int:pk>/update/', views.shoe_update, name='shoe_update'),
    path('shoe/<int:pk>/delete/', views.shoe_delete, name='shoe_delete'),
]