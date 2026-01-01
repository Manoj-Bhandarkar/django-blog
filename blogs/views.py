from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category, Comment
from django.db.models import Q


def posts_by_category(request, category_id):
    # fetch posts by category_id logic here
    posts = Blog.objects.filter(status="Published", category=category_id)
    # based on the category_id fetch name from Category model
    # category DoesNotExit redirect to home page
    # try:
    # category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect("home")

	# use get_object_or_404 when you want show 404 error page instead of redirecting
    # 404 approach	
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
        #return redirect("blog_detail", slug=slug)
        # or use HttpResponseRedirect
        # from django.http import HttpResponseRedirect  
        return HttpResponseRedirect(request.path_info)
    #comment section
    comments = Comment.objects.filter(blog=single_blog)
    context = {
        "single_blog": single_blog,
        "comments": comments,
    }
    return render(request, "blog_detail.html", context)

def blog_search(request):
    keyword = request.GET.get("keyword")
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published") if keyword else []     
    context = {
        "blogs": blogs,
        "keyword": keyword,
    }
    return render(request, "blog_search.html", context)
