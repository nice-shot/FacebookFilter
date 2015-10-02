from django.test import TestCase
from .serializers import FilterSerializer

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
        f = FilterSerializer(data=filter_data)
        self.assertTrue(f.is_valid())
