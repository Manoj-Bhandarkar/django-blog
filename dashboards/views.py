from django.shortcuts import render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    categorys_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        'categorys_count': categorys_count,
        'blogs_count': blogs_count
    }
    return render(request, 'dashboards/dashboard.html', context)

@login_required(login_url='login')
def dashboard_categories(request):
   # not required to fetch category because context processor is used
    return render(request, 'dashboards/dashboard_categories.html')


