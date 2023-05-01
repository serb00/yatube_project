# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница со списком постов в группе
    path('group/', views.group_posts, name='groups'),
    path('group/<slug>/', views.group_posts, name='groups'),
    # Отдельная страница с информацией о сорте мороженого
    path('group/<int:pk>/', views.group_detail, name='group_detail'),
]
