from django.test import SimpleTestCase, TestCase
from .models import Transaction
from django.urls import reverse
from datetime import datetime

# Create your tests here.
class ReportPageViewTest(TestCase):
    def setUp(self):
        Transaction.objects.create(timestamp=datetime.now(), visa="Tourist", pax=2)
        
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_view_url_by_name(self):
        response = self.client.get(reverse("report"))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("report"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "report.html")


class TransactionModelTest(TestCase):
    def setUp(self):
        Transaction.objects.create(timestamp=datetime.now(), visa="Tourist", pax=2)
    
    def test_visa_content(self):
        transaction = Transaction.objects.get(id=1)
        visa = str(transaction.visa)
        self.assertEqual(visa, "Tourist")