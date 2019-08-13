from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('posts', views.ListPosts.as_view(), name='posts'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
]
