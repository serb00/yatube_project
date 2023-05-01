# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Импортируем загрузчик.
# from django.template import loader

# Create your views here.
# Главная страница


def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    # template = loader.get_template('ice_cream/index.html')
    # Формируем шаблон
    # return HttpResponse(template.render({}, request))
    #
    # same but using django shortcuts
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text,
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
