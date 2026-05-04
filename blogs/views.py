from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category, Comment, Status
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector
from django.db.models import Count, Q, Prefetch


def posts_by_category(request, slug):
    category = Category.objects.filter(slug=slug).first()
    if not category:
        return render(request, "404.html", status=404)

    posts = Blog.objects.select_related("category", "author").filter(
        status=Status.PUBLISHED, category__slug=slug
    )
    categories = Category.objects.annotate(
        post_count=Count("blogs", filter=Q(blogs__status=Status.PUBLISHED))
    ).filter(post_count__gt=0)

    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    context = {
        "posts": posts,
        "category": category,
        "categories": categories,
    }
    return render(request, "posts_by_category.html", context)


def blog_detail(request, slug):
    single_blog = get_object_or_404(
        Blog.objects.select_related("category", "author").prefetch_related(
            Prefetch(
                "comments",
                queryset=Comment.objects.select_related("user")
                .filter(is_approved=True)
                .order_by("-created_at"),
            )
        ),
        slug=slug,
        status=Status.PUBLISHED,
    )
    categories = Category.objects.annotate(
        post_count=Count("blogs", filter=Q(blogs__status=Status.PUBLISHED))
    ).filter(post_count__gt=0)

    ## Handle comment submission
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(f"/login/?next={request.path}")
        content = request.POST.get("comment", "").strip()
        # Validation FIRST
        if not content:
            messages.error(request, "Comment cannot be empty")
            return HttpResponseRedirect(request.path_info)

        if len(content) < 3:
            messages.error(request, "Comment must be at least 3 characters")
            return HttpResponseRedirect(request.path_info)

        # Save comment
        Comment.objects.create(
            user=request.user, blog=single_blog, comment=content, is_approved=True
        )

        messages.success(request, "Comment added successfully!")
        return HttpResponseRedirect(request.path_info)

    context = {
        "single_blog": single_blog,
        "categories": categories,
    }
    return render(request, "blog_detail.html", context)


def blog_search(request):
    keyword = request.GET.get("keyword").strip()
    if keyword:
        blogs = (
            Blog.objects.annotate(
                search=SearchVector("title", "short_description", "blog_body"),
            )
            .filter(search=keyword, status=Status.PUBLISHED)
            .select_for_update("category", "author")
        )
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


def all_categories(request):
    categories = Category.objects.all()
    return render(request, "all_categories.html", {"categories": categories})
