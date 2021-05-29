from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    """Пост"""
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор')
    title = models.CharField("Название поста", max_length=300)
    slug = models.SlugField('Url', max_length=255, unique=True)
    content = models.TextField('Контент', blank=True)
    image = models.ImageField("Изображение", upload_to='posts/', blank=True,
                              null=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']


class About(models.Model):
    """О нас"""
    title = models.CharField('Название', max_length=200)
    content = models.TextField('Контент')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
