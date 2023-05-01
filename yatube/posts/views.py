# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post

# Create your views here.
# Главная страница


def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = 'posts/index.html'

    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }

    return render(request, template, context)


# Страница со списком мороженого
def groups_list(request):
    template = 'posts/groups_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context)


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_detail(request, pk):
    return HttpResponse(f'Группа номер {pk}')
