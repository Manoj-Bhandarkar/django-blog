from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('created_at')
    posts = Blog.objects.filter(is_featured=False, status='Published').order_by('created_at')
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'home.html', context)
    