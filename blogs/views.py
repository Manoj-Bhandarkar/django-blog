from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category, Comment, Status
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector


def posts_by_category(request, category_id):
    posts = Blog.objects.select_related("category", "author").filter(
        status=Status.PUBLISHED, category_id=category_id
    )

    category = get_object_or_404(Category, pk=category_id)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    context = {
        "posts": posts,
        "category": category,
    }
    return render(request, "posts_by_category.html", context)


def blog_detail(request, slug):
    single_blog = get_object_or_404(
        Blog.objects.select_related("category", "author").prefetch_related(
            "comments__user"
        ),
        slug=slug,
        status=Status.PUBLISHED,
    )

    if request.method == "POST":
        comment = Comment()
        if request.user.is_authenticated:
            comment.user = request.user
        else:
            return redirect(f"/login/?next={request.path}")
        comment.blog = single_blog
        content = request.POST.get("comment", "").strip()
        if content:
            comment.comment = content
            messages.success(request, "Comment submitted for approval")
            comment.save()

        return HttpResponseRedirect(request.path_info)
    # comment section
    comments = (
        Comment.objects.select_related("user")
        .filter(blog=single_blog, is_approved=True)
        .order_by("-created_at")
    )
    context = {
        "single_blog": single_blog,
        "comments": comments,
    }
    return render(request, "blog_detail.html", context)


def blog_search(request):
    keyword = request.GET.get("keyword").strip()
    if keyword:
        blogs = Blog.objects.annotate(
            search=SearchVector("title", "short_description", "blog_body"),
        ).filter(search=keyword, status=Status.PUBLISHED)
    else:
        blogs = Blog.objects.none()

    paginator = Paginator(blogs, 5)
    page = request.GET.get("page")
    blogs = paginator.get_page(page)
    context = {
        "blogs": blogs,
        "keyword": keyword,
    }
    return render(request, "blog_search.html", context)
