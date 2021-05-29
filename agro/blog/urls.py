from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', views.PostList.as_view(), name='post_list'),
    path('about/', views.AboutAsView.as_view(), name='about'),
    path('post/<str:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]
