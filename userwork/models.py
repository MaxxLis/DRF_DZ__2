from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    email_autor = models.EmailField('Email', unique=True, max_length=64)

    def __str__(self):
        return f'Пользовательь {self.last_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

