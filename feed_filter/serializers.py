from rest_framework import serializers
from feed_filter.models import FacebookPage, Filter, Post, FilteredPost
from django.contrib.auth.models import User

def retrieve_page(page_data):
    """
    :param page_data: Details for a facebook page - keys are "id" and "name"
    :type page_data: dict
    :return: A facebook page that's either created or updated
    :rtype: FaceBookPage
    """
    # This may cause a problem where some group names are overriden. Should find
    # a smarter solution
    page, created = FacebookPage.objects.update_or_create(
        defaults={"name": page_data["name"]},
        id=page_data["id"]
    )
    return page


class FacebookPageSerializer(serializers.ModelSerializer):
    # Used to remove the unique validator
    id = serializers.CharField(max_length=100,
                               help_text="Page's facebook id")

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
            new_filter.pages.add(retrieve_page(page_data))
        new_filter.save()
        return new_filter

    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        instance.name = validated_data.get("name", instance.name)
        instance.filter_str = validated_data.get("filter_str",
                                                 instance.filter_str)
        if "pages" in validated_data:
            instance.pages.clear()
            for page_data in validated_data["pages"]:
                instance.pages.add(retrieve_page(page_data))

        instance.save()
        return instance



class FilteredPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilteredPost
