from django.test import TestCase
from .serializers import FilterSerializer
from .models import Filter

# Create your tests here.
class SerializersTests(TestCase):
    fixtures = ['single_user.json']

    def test_filter_creation(self):
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
