from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, PostForm, UserForm, EditUserForm
from django.contrib.auth.models import User

# ---------------- DASHBOARD ----------------

@login_required(login_url="login")
def dashboard(request):
    categories_count = Category.objects.count()
    blogs_count = Blog.objects.count()
    context = {"categories_count": categories_count, "blogs_count": blogs_count}
    return render(request, "dashboards/dashboard.html", context)


# ---------------- CATEGORY ----------------

@login_required(login_url="login")
def categories(request):
    categories_list = Category.objects.all().order_by('-created_at')
    context = {"categories": categories_list}
    return render(request, "dashboards/categories.html", context)


@login_required(login_url="login")
def add_category(request):
    if not request.user.is_staff:
        return redirect("dashboard")
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    else:
        form = CategoryForm()
        context = {"form": form}
    return render(request, "dashboards/add_category.html", context)


@login_required(login_url="login")
def edit_category(request, pk):
    if not request.user.is_staff:
        return redirect("dashboard")
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


@require_POST
@login_required(login_url="login")
def delete_category(request, pk):
    if not request.user.is_staff:
        return redirect("dashboard")
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("categories")


# ---------------- POSTS ----------------


@login_required(login_url="login")
def posts(request):
    if request.user.is_staff:
        posts = Blog.objects.all()
    else:
        posts = Blog.objects.filter(author=request.user)
    context = {"posts": posts}
    return render(request, "dashboards/posts.html", context)


@login_required(login_url="login")
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()  # Save to get the ID
            messages.success(request, "Post created")
            return redirect("posts")
    else:
        form = PostForm()
        context = {"form": form}
    return render(request, "dashboards/add_post.html", context)


@login_required(login_url="login")
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if not request.user.is_staff and post.author != request.user:
        return redirect("dashboard")
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect("posts")
    else:
        form = PostForm(instance=post)
    context = {"form": form, "post": post}
    return render(request, "dashboards/edit_post.html", context)


@require_POST
@login_required(login_url="login")
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if not (request.user.is_staff or request.user.is_superuser):
        return redirect("dashboard")
    if request.method == "POST":
        post.delete()
    return redirect("posts")

# ---------------- USERS ----------------

@login_required(login_url="login")
def users(request):
    if not request.user.is_superuser:
        return redirect("dashboard")
    users = User.objects.all()
    context = {"users": users}
    return render(request, "dashboards/users.html", context)


@login_required(login_url="login")
def add_user(request):
    if not request.user.is_superuser:
        return redirect("dashboard")
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users")
        else:
            print(form.errors)
    else:
        form = UserForm()
        context = {"form": form}
        return render(request, "dashboards/add_user.html", context)


@login_required(login_url="login")
def edit_user(request, pk):
    if not request.user.is_superuser:
        return redirect("dashboard")
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("users")
    else:
        form = EditUserForm(instance=user)
    context = {"form": form, "selected_user": user}
    return render(request, "dashboards/edit_user.html", context)


@require_POST
@login_required(login_url="login")
def delete_user(request, pk):
    if not request.user.is_superuser:
        return redirect("users")
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect("users")
