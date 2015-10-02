from django.db import models
from django.contrib.auth import models as auth_models
from jsonfield import JSONCharField

# Create your models here.

class FacebookPage(models.Model):
    """
    Represents a Facebook page, group or any other object that we can subscribe
    to
    """
    id = models.CharField(max_length=100, primary_key=True,
                          help_text="Page's facebook id")
    name = models.CharField(max_length=300, blank=True,
                            help_text="Page or group's name")

class Filter(models.Model):
    """
    Filter settings for a specific user
    """
    user = models.ForeignKey(auth_models.User, related_name="filters")
    filter_str = JSONCharField(max_length=1000)
    # FacebookPage does not have back relation to Filter
    pages = models.ManyToManyField(FacebookPage, related_name="+",
                                   help_text="Pages to follow")


class Post(models.Model):
    """
    Facebook post that we found relevant
    """
    id = models.CharField(max_length=100, primary_key=True,
                          help_text="Facebook post id")
    page = models.ForeignKey(FacebookPage, help_text="Page this post is from")
    message = models.TextField()
    user = models.CharField(max_length=300,
                            help_text="Post creator's user name")
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    filters = models.ManyToManyField(Filter, through="FilteredPost",
                                     related_name="posts")

class FilteredPost(models.Model):
    """
    Relation between filter and post. This includes the user's comment and
    whether the post is interesting
    """
    filter = models.ForeignKey(Filter)
    post = models.ForeignKey(Post)
    found_time = models.DateTimeField(auto_now_add=True)
    keep = models.NullBooleanField()
    comment = models.TextField(blank=True)
