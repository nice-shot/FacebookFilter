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
        pages = []
        for page_data in pages_data:
            # This may cause a problem were some group names are overriden. We
            # should find a smarter solution
            # TODO: Make this work!
            page = FacebookPage.objects.update_or_create(
                defaults={"name": page_data["name"]},
                id=page_data["id"]
            )[0]
            pages.append(page)
        return Filter.objects.create(pages=pages, **validated_data)


class FilteredPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilteredPost
