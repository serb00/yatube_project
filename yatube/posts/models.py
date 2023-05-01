from django.db import models
# Из модуля auth импортируем функцию get_user_model
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='groups',
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.text
