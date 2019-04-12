from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': 'Kurt',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 6, 2019'
    },
{
        'author': 'Donovan',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 8, 2019'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})




