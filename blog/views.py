from django.shortcuts import render
from .models import Post


def blog_view_post(request, post_id):
    queryset_list = Post.objects.all().order_by("-date")
    detail = Post.objects.get(id=post_id)

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(title__icontains=query)

    context = {"object_list": queryset_list, "detail": detail}
    return render(request, 'blog/blog.html', context)


# def blog_view_detail(request, post_id):
#     post = Post.objects.get(id=post_id)
#     return render(request, 'blog/post.html', {'post': post})
