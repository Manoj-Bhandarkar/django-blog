from .models import Category
from about.models import SocialLink
from django.core.cache import cache
from django.db.models import Count, Q

def get_categories(request):
    categories = cache.get("global_categories")
    if not categories:
        categories = Category.objects.annotate(
            post_count=Count("blogs", filter=Q(blogs__status="published"))
        ).filter(post_count__gt=0)
        cache.set("global_categories", categories, 60 * 60)
    return {"categories": categories}\

def get_social_links(request):
    social_links = cache.get_or_set(
        "social_links_list", SocialLink.objects.all(), 60 * 60
    )
    return {'social_links': social_links}