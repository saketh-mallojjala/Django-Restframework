from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice, InvoiceDetail


class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(date='2024-01-01', customer_name='Test Customer')
        self.invoice_detail_data = {'description': 'Test Item', 'quantity': 2, 'unit_price': 10.0, 'price': 20.0}

    def test_create_invoice(self):
        data = {'date': '2024-02-01', 'customer_name': 'New Customer'}
        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invoice_with_details(self):
        data = {'date': '2024-02-01', 'customer_name': 'New Customer', 'invoice_details': [self.invoice_detail_data]}
        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InvoiceDetail.objects.count(), 1)

    def test_update_invoice(self):
        data = {'date': '2024-02-01', 'customer_name': 'Updated Customer'}
        response = self.client.put(f'/invoices/{self.invoice.pk}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.invoice.refresh_from_db()
        self.assertEqual(self.invoice.customer_name, 'Updated Customer')

    # Add more test cases for other CRUD operations and edge cases
