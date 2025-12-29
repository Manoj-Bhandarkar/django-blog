from django.shortcuts import redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm

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
def categories(request):
   # not required to fetch category because context processor is used
    return render(request, 'dashboards/categories.html')

@login_required(login_url='login')  
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form=CategoryForm()
        context = {
            'form': form
        }
    return render(request, 'dashboards/add_category.html', context)
        


