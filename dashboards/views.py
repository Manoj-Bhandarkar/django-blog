from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm, PostForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

@login_required(login_url="login")
def dashboard(request):
    categorys_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {"categorys_count": categorys_count, "blogs_count": blogs_count}
    return render(request, "dashboards/dashboard.html", context)


@login_required(login_url="login")
def categories(request):
    # not required to fetch category because context processor is used
    return render(request, "dashboards/categories.html")


@login_required(login_url="login")
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    else:
        form = CategoryForm()
        context = {"form": form}
    return render(request, "dashboards/add_category.html", context)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("categories")
    else:
        form = CategoryForm(instance=category)
    context = {"form": form, "category": category}
    return render(request, "dashboards/edit_category.html", context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("categories")


def posts(request):
    posts = Blog.objects.filter(status="Published")
    context = {"posts": posts}
    return render(request, "dashboards/posts.html", context)


@login_required(login_url="login")
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save() # Save to get the ID    
            title = form.cleaned_data["title"]  # Generate slug using title 
            post.slug = slugify(title) + "-" + str(post.id) # Unique slug by appending ID
            post.save()
            return redirect("posts")
    else:
        form = PostForm()
        context = {"form": form}
    return render(request, "dashboards/add_post.html", context)

@login_required(login_url="login")
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data["title"]  # Update slug using title
            post.slug = slugify(title) + "-" + str(post.id) # Update slug if title changed
            post.save()
            return redirect("posts")
    else:
        form = PostForm(instance=post)
    context = {"form": form, "post": post}
    return render(request, "dashboards/edit_post.html", context)        

@login_required(login_url="login")
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect("posts")

@login_required(login_url="login")
def users(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "dashboards/users.html", context) 