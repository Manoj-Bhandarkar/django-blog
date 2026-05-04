from django.shortcuts import redirect, render
from about.models import About
from .forms import RegistrationForm
from blogs.models import Blog, Category, Status
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
from django.core.paginator import Paginator
from django.contrib.auth import login as auth_login
from django.core.cache import cache
from django.db.models import Count, Q


def home(request):
    featured_posts = (
        Blog.objects.select_related("category", "author")
        .filter(is_featured=True, status=Status.PUBLISHED)
        .order_by("-created_at")
    )
    posts = (
        Blog.objects.select_related("category", "author")
        .filter(is_featured=False, status=Status.PUBLISHED)
        .order_by("-created_at")
    )
    categories = cache.get_or_set(
        "categories_with_counts",
        Category.objects.annotate(
            post_count=Count("blogs", filter=Q(blogs__status="published"))
        ).filter(post_count__gt=0),
        86400,
    )
    hero_post = featured_posts.first()
    other_featured_posts = featured_posts[1:]
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    # fetch about us information
    try:
        about = cache.get_or_set("about_data", About.objects.first(), 86400)
    except About.DoesNotExist:
        about = None

    context = {
        "featured_posts": featured_posts,
        "posts": posts,
        "about": about,
        "categories": categories,
        "hero_post": hero_post,
        "other_featured_posts": other_featured_posts,
    }
    return render(request, "home.html", context)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("login")
    else:
        form = RegistrationForm()
    context = {
        "form": form,
    }
    return render(request, "register.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "login.html", context)


def logout(request):
    auth.logout(request)
    return redirect("home")

def custom_404(request, exception):
    return render(request, "404.html", status=404)