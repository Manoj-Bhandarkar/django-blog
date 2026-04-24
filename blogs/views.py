from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category, Comment
from django.db.models import Q


def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status="Published", category=category_id)

    category = get_object_or_404(Category, pk=category_id)

    context = {
        "posts": posts,
        "category": category,
    }
    return render(request, "posts_by_category.html", context)


def blog_detail(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status="Published")
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST["comment"]
        comment.save()
        return HttpResponseRedirect(request.path_info)
    # comment section
    comments = Comment.objects.filter(blog=single_blog)
    context = {
        "single_blog": single_blog,
        "comments": comments,
    }
    return render(request, "blog_detail.html", context)


def blog_search(request):
    keyword = request.GET.get("keyword")
    blogs = (
        Blog.objects.filter(
            Q(title__icontains=keyword)
            | Q(short_description__icontains=keyword)
            | Q(blog_body__icontains=keyword),
            status="Published",
        )
        if keyword
        else []
    )
    context = {
        "blogs": blogs,
        "keyword": keyword,
    }
    return render(request, "blog_search.html", context)
