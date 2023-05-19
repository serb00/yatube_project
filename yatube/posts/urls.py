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
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/', views.post_details, name='post_details'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('posts/create', views.post_create, name="post_create"),
]
