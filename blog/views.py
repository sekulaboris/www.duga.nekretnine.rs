from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag

def base(request):
    return render (request,
                    'base.html')

def post_list(request, tag_slug=None):
    posts= Post.published.all()
    tag=None

    if tag_slug:
        tag=get_object_or_404(Tag, slug=tag_slug)
        posts= posts.filter(tags__in=[tag])
    return render(request,
                    'list.html',
                    {'posts':posts,
                    'tag':tag})

def post_detail(request, year, month, day, post):
    post=get_object_or_404(Post, slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    return render(request,
                    'detail.html',
                    {'post':post})

# Create your views here.
