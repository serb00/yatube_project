# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница со списком сортов мороженого
    path('groups/', views.groups_list, name='groups'),
    # Отдельная страница с информацией о сорте мороженого
    path('groups/<int:pk>/', views.group_detail, name='group_detail'),
]
