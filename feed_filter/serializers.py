from rest_framework import serializers
from feed_filter.models import FacebookPage, Filter, Post, FilteredPost
from django.contrib.auth.models import User


class FacebookPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookPage

class FilterSerializer(serializers.ModelSerializer):
    pages = FacebookPageSerializer(many=True)

    class Meta:
        model = Filter

    def create(self, validated_data):
        # TODO - Add create and update methods to handle page creation
        pages_data = validated_data.pop("pages")
        feed_filter = Filter.objects.create

class FilteredPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilteredPost
