from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(unique=True, max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        indexes = [models.Index(fields=["slug"])]

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.category_name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Status(models.TextChoices):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published", "Published"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="blogs"
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    featured_image = models.ImageField(
        upload_to="uploads/%Y/%m/%d", null=True, blank=True
    )
    short_description = models.CharField(max_length=500)
    blog_body = models.TextField()
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.status})"

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["status", "is_featured"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)  # Save to get the ID
            self.slug = f"{self.slug}-{self.id}"
            super().save(update_fields=["slug"])
        else:
            super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment[:50]
        # return f'Comment by {self.user.username} on {self.blog.title}'

    class Meta:
        indexes = [models.Index(fields=["created_at"])]
