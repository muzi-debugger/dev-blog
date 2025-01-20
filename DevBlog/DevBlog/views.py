from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required

from .import forms
# Create your views here.

def homePage(request):
    return render(request, 'home.html')

def aboutPage(request):
    return render(request, 'about.html')

def post_list(request):
    posts = Post.objects.all().order_by('-date')[:5]
    return render(request, 'posts/posts_list.html', {'post': posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})

@login_required(login_url='/user/login/')
def new_post(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save with user
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('post_list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/new_post.html', {'form': form})