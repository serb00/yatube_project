# from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator

from core.functions.decorators import authorized_only
from .forms import PostCreationForm
from .models import Group, Post, User


# Create your views here.
# Главная страница
@authorized_only
def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = 'posts/index.html'

    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (по убыванию)
    posts = Post.objects.order_by('-pub_date')

    # add paginator
    paginator = Paginator(posts, 10)
    # getting page number from URL Get request
    page_number = request.GET.get("page")
    # getting that page from paginator
    page_obj = paginator.get_page(page_number)

    # В словаре context отправляем информацию в шаблон
    context = {
        'page_obj': page_obj,
        'header': 'Posts'
    }

    return render(request, template, context)


@authorized_only
def group_posts(request, slug=None):
    template = 'posts/group_list.html'
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
    posts = Post.objects.filter(group=group).order_by('-pub_date')

    # add paginator
    paginator = Paginator(posts, 10)
    # getting page number from URL Get request
    page_number = request.GET.get("page")
    # getting that page from paginator
    page_obj = paginator.get_page(page_number)

    context = {
        'group': group,
        'page_obj': page_obj
    }
    return render(request, template, context)


def profile(request, username):
    template = 'posts/profile.html'

    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user).order_by('-pub_date')[:10]

    # paginator = Paginator(posts, 10)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)

    context = {
        'user': user,
        'posts': posts
    }

    return render(request, template, context)


def post_details(request, post_id):
    template = 'posts/post_details.html'
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, template, context)


@authorized_only
def post_create(request):
    template = 'posts/post_create.html'
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        user = User.objects.get(username=request.user.username)
        if form.is_valid():
            post_instance = form.save(commit=False)
            post_instance.text = form.cleaned_data['text']
            post_instance.group = form.cleaned_data['group']
            post_instance.author = user

            post_instance.save()
            return redirect(f'/profile/{request.user.username}')
        return render(request, template, {'form': form})

    form = PostCreationForm()

    context = {
        "form": form
    }
    return render(request, template, context)


@authorized_only
def post_edit(request, post_id):
    template = 'posts/post_create.html'
    post = get_object_or_404(Post, pk=post_id)
    form = PostCreationForm(request.POST or None, instance=post)
    if request.method == 'POST':
        # form = PostCreationForm(request.POST)
        user = User.objects.get(username=request.user.username)
        # group = get_object_or_404(Group, title=form.cleaned_data['group'])
        if form.is_valid():
            post_instance = form.save(commit=False)
            post_instance.text = form.cleaned_data['text']
            post_instance.group = form.cleaned_data['group']
            post_instance.author = user

            post_instance.save()
            return redirect(f'/profile/{request.user.username}')
        return render(request, template, {'form': form})

    is_edit = request.user == post.author

    if not is_edit:
        return redirect(f'/posts/{post.pk}')

    context = {
        "form": form,
        "is_edit": is_edit,
        "post": post
    }
    return render(request, template, context)
