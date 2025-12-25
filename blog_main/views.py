from django.shortcuts import render
from about.models import About
from .forms import RegistrationForm
from blogs.models import Category, Blog


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status="Published").order_by("created_at")
    posts = Blog.objects.filter(is_featured=False, status="Published").order_by("created_at")
    # fetch about us information
    try:
        about = About.objects.get()
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
            form.save()
            return render(request, "registration_success.html")
    else:
            form = RegistrationForm()    
    context = {
        "form": form,
    }
    return render(request, "register.html", context)