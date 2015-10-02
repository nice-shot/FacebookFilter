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
        pages_data = validated_data.pop("pages")
        new_filter = Filter.objects.create(**validated_data)
        for page_data in pages_data:
            # This may cause a problem were some group names are overriden. We
            # should find a smarter solution
            page = FacebookPage.objects.update_or_create(
                defaults={"name": page_data["name"]},
                id=page_data["id"]
            )[0]
            new_filter.pages.add(page)
        return new_filter


class FilteredPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilteredPost
