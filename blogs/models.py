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

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    indexes = [models.Index(fields=["slug"])]


class Status(models.TextChoices):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published", "Published"


status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
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
        return self.title

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["status", "is_featured"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)  # get ID first
            self.slug = f"{slugify(self.title)}-{self.id}"
            return super().save(update_fields=["slug"])
        super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User,  null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(max_length=250)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment[:50]
        # return f'Comment by {self.user.username} on {self.blog.title}'

    class Meta:
        indexes = [
            models.Index(fields=['created_at'])
        ]
