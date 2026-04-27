from .models import Category
from about.models import SocialLink
from django.core.cache import cache

def get_categories(request):
    categories = cache.get('global_categories')
    if not categories:
        categories = Category.objects.only("id", "category_name", "slug")
        cache.set('global_categories', categories, 60 * 60)  # Cache for 1 hour
    return dict(categories=categories)

def get_social_links(request):
    social_links = cache.get_or_set('social_links_list', SocialLink.objects.all(), 60 * 60)
    return dict(social_links=social_links)