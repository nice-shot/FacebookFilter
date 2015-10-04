from django.test import TestCase
from .serializers import FilterSerializer
from .models import Filter, FacebookPage

# Create your tests here.
class SerializersTests(TestCase):
    fixtures = ['single_user.json']

    def test_filter_creation_and_update(self):
        """
        By creating the filter the FacebookPages should also be created
        """
        filter_data = {
            "pages": [
                {"id": "123124124", "name": "Bla"},
                {"id": "12312444", "name": "Yada"},
            ],
            "filter_str": '["hello", "again"]',
            "user": 1,
            "name": "Some filter",
        }
        filter_serialize = FilterSerializer(data=filter_data)
        self.assertTrue(filter_serialize.is_valid())
        new_filter = filter_serialize.save()
        self.assertEqual(Filter.objects.count(), 1)
        updated_data = {
            "filter_str": '["friend", "of a friend"]',
            "pages": [
                {"id": "123124124", "name": "Bla"},
                {"id": "421421", "name": "Wawa"},
            ],
        }
        filter_serialize = FilterSerializer(new_filter, data=updated_data,
                                            partial=True)
        self.assertTrue(filter_serialize.is_valid())
        updated_filter = filter_serialize.save()
        self.assertEqual(updated_filter, new_filter)
        # Make sure we only have 3 FacebookPages
        self.assertEqual(FacebookPage.objects.count(), 3)
