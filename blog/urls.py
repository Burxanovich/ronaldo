from django.urls import path
from .views import blog_detail, blog_list

app_name = 'blog'

urlpatterns = [
    path('article<slug:slug>/', blog_detail, name='detail'),
    path("blog-list/", blog_list, name='list')
]
