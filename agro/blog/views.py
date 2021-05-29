from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from .models import Post, About


class HomeView(View):
    """Главная страница"""
    def get(self, request, *args, **kwargs):
        info = About.objects.order_by('-id')
        posts = Post.objects.order_by('-id')[:3]
        context = {
            'info': info,
            'posts': posts
        }
        return render(request, 'blog/index.html', context)


class PostList(ListView):
    """Список постов"""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6


class PostDetailView(DetailView):
    """Конкретный пост"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'


class AboutAsView(View):
    """Вывод информации на странице 'О нас'"""
    def get(self, request, *args, **kwargs):
        info = About.objects.order_by('-id')
        posts = Post.objects.order_by('-id')[:3]
        context = {
            'info': info,
            'posts': posts
        }
        return render(request, 'blog/about.html', context)
