from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.

class Filter(models.Model):
    """
    Filter settings for a specific user
    """
    user = models.ForeignKey(auth_models.User, related_name="filters")
    relative_id = models.PositiveIntegerField(help_text="Unique filter ID per user")
    filter_str = models.CharField(max_length=1000)

    class Meta:
        unique_together = (("user", "relative_id"),)

class Post(models.Model):
    """
    Facebook post that we found relevant
    """
    id = models.CharField(max_length=100, primary_key=True,
                          help_text="Facebook post id")
    message = models.TextField()
    user = models.CharField(max_length=300, help_text="Facebook user name")
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    filters = models.ManyToManyField(Filter, through="FilteredPost",
                                     related_name="posts")

class FilteredPost(models.Model):
    """
    Relation between filter and post
    """
    filter = models.ForeignKey(Filter)
    post = models.ForeignKey(Post)
    found_time = models.DateTimeField(auto_now_add=True)
    interesting = models.NullBooleanField()
    comment = models.TextField(blank=True)
