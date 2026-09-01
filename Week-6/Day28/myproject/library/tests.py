from django.test import TestCase


class BookURLTests(TestCase):
    def test_homepage_is_available_at_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_book_detail_page_is_available(self):
        response = self.client.get('/book/1/')
        self.assertEqual(response.status_code, 200)


    
