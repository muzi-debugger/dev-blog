from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.

def homePage(request):
    return render(request, 'home.html')

def aboutPage(request):
    return render(request, 'about.html')

def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'post': posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})

@login_required(login_url='/user/login/')
def new_post(request):
    return render(request, 'posts/new_post.html')