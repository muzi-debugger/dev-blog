from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'home.html')

def aboutPage(request):
    return render(request, 'about.html')

def post_list(request):
    return render(request, 'posts/posts_list.html')