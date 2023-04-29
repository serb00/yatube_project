# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком сортов мороженого
    path('groups/', views.groups_list),
    # Отдельная страница с информацией о сорте мороженого
    path('groups/<int:pk>/', views.group_detail),
]
