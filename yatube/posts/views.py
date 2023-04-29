from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Главная страница


def index(request):
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def groups_list(request):
    return HttpResponse('Список групп')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_detail(request, pk):
    return HttpResponse(f'Группа номер {pk}')
