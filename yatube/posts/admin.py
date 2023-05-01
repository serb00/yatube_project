from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('text', 'pub_date', 'author')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка 
    empty_value_display = '-empty-'


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)
