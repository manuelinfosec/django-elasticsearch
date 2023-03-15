from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name}"


ARTICLE_TYPES = [
    ("UN", "Unspecified"),
    ("TU", "Tutorial"),
    ("RS", "Research"),
    ("RW", "Review")
]

class Article(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=ARTICLE_TYPES, default="UN")
    categories = models.ManyToManyField(to=Category, blank=True, related_name="categories")
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def type_to_string(self):
        if self.type == "UN":
            return ARTICLE_TYPES[0][1]
        elif self.type == "TU":
            return ARTICLE_TYPES[1][1]
        elif self.type == "RS":
            return ARTICLE_TYPES[2][1]
        elif self.type == "RW":
            return ARTICLE_TYPES[3][1]

    def __str__(self):
        return f"{self.author}: {self.title} ({self.created_datetime.date()})"
