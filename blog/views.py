from django.shortcuts import render, get_object_or_404
from .models import Post
from django.urls import reverse

#------------------sa ovim kodom pikazujem listu postova koji su objavljeni -----------------------
def post_list(request):
    posts = Post.published.all()
    return render(request,
                    'blog/post/list.html',
                    {'posts': posts})

#----------------sa ovim kodom prikazujem jedan post ------------------------------
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                    'blog/post/detail.html',
                    {'post': post})


