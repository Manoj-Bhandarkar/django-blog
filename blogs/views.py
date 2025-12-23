from django.shortcuts import redirect, render

from .models import Blog, Category


def posts_by_category(request, category_id):
    # fetch posts by category_id logic here
    posts = Blog.objects.filter(status="Published", category=category_id)
    # based on the category_id fetch name from Category model
    # category DoesNotExit redirect to home page
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect("home")

    context = {
        "posts": posts,
        "category": category,
    }
    return render(request, "posts_by_category.html", context)
