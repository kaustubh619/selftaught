from django.urls import path
from .views import blog_view_post

urlpatterns = [
    path('', blog_view_post, name='blog'),
    path('<int:post_id>/', blog_view_post, name='post')
]
