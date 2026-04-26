from django.shortcuts import redirect, render
from about.models import About
from .forms import RegistrationForm
from blogs.models import Blog, Status
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
from django.core.paginator import Paginator
from django.contrib.auth import login as auth_login

def home(request):
    featured_posts = Blog.objects.select_related('category', 'author').filter(is_featured=True, status=Status.PUBLISHED).order_by(
        "-created_at"
    )
    posts = Blog.objects.select_related('category', 'author').filter(is_featured=False, status=Status.PUBLISHED).order_by(
        "-created_at"
    )
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    # fetch about us information
    try:
        about = About.objects.first()
    except About.DoesNotExist:
        about = None

    context = {
        "featured_posts": featured_posts,
        "posts": posts,
        "about": about,
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
