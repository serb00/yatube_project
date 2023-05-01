# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Group, Post

# Create your views here.
# Главная страница


def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = 'posts/index.html'

    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (по убыванию)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'text': 'Header'
    }

    return render(request, template, context)


def group_posts(request, slug=None):
    template = 'posts/group_list.html'
    text = slug
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    if slug is None:
        group = None
    else:
        group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'text': text,
    }
    return render(request, template, context)


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_detail(request, pk):
    return HttpResponse(f'Группа номер {pk}')
