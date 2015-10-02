from rest_framework import serializers
from feed_filter.models import Filter, Post, FilteredPost
from django.contrib.auth.models import User


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter

class FilteredPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilteredPost
