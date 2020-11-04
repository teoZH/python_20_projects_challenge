from django.shortcuts import render, get_object_or_404
from blog_app.models import Post
from django.http import HttpResponse


# Create your views here.


def homepage(request):
    context = {}
    posts = Post.objects.all()
    if posts:
        context = {
            'posts': posts[1:],
            'last_post': posts[0]
        }
    return render(request, 'base.html', context)


def articles(request):
    context = {}
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'article.html', context)


def details(request, art_id, slug):
    post = get_object_or_404(Post, pk=art_id)
    return render(request, 'details.html', {'post': post})
