from django.views import View
from .models import Invoice, InvoiceDetail
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.http import JsonResponse
from django.core.serializers import serialize


@method_decorator(csrf_exempt, name='dispatch')
class AddInvoiceView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)

            # Extract invoice data
            date = data.get('date')
            customer_name = data.get('customer_name')

            # Create invoice instance
            invoice = Invoice.objects.create(date=date, customer_name=customer_name)

            # Extract and save invoice details
            details = data.get('details', [])
            for detail_data in details:
                description = detail_data.get('description')
                quantity = detail_data.get('quantity')
                unit_price = detail_data.get('unit_price')

                InvoiceDetail.objects.create(invoice=invoice, description=description, quantity=quantity,
                                             unit_price=unit_price)

            return JsonResponse({'success': True, 'message': 'Invoice added successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})


class ViewInvoiceView(View):
    def get(self, request, *args, **kwargs):
        invoices = Invoice.objects.all()
        serialized_invoices = []

        for invoice in invoices:
            details = [{
                'description': detail.description,
                'quantity': detail.quantity,
                'unit_price': detail.unit_price,
                'price': detail.price,
            } for detail in invoice.invoicedetail_set.all()]

            serialized_invoice = {
                'id': invoice.id,
                'date': invoice.date,
                'customer_name': invoice.customer_name,
                'details': details,
            }

            serialized_invoices.append(serialized_invoice)

        return JsonResponse({'invoices': serialized_invoices}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class DeleteInvoiceView(View):
    def get(self, request, invoice_id, *args, **kwargs):
        try:
            invoice = Invoice.objects.get(id=invoice_id)
            invoice.delete()
            return JsonResponse({'success': True, 'message': f'Invoice {invoice_id} successfully deleted'})
        except Invoice.DoesNotExist:
            return JsonResponse({'success': False, 'message': f'Invoice with ID {invoice_id} does not exist'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})


@method_decorator(csrf_exempt, name='dispatch')
class UpdateInvoiceView(View):
    def patch(self, request, invoice_id, *args, **kwargs):
        try:
            data = json.loads(
                request.body.decode('utf-8'))  # Assuming you are sending the updated data via PATCH request
            invoice = Invoice.objects.get(id=invoice_id)

            # Update invoice details
            invoice.date = data.get('date', invoice.date)
            invoice.customer_name = data.get('customer_name', invoice.customer_name)
            invoice.save()

            # Update invoice details
            details_data = data.get('details', [])
            for detail_data in details_data:
                detail_id = detail_data.get('id')
                description = detail_data.get('description')
                quantity = detail_data.get('quantity')
                unit_price = detail_data.get('unit_price')

                if detail_id:
                    # If detail_id is provided, update existing detail
                    detail = InvoiceDetail.objects.get(id=detail_id, invoice=invoice)
                    if description is not None:
                        detail.description = description
                    if quantity is not None:
                        detail.quantity = quantity
                    if unit_price is not None:
                        detail.unit_price = unit_price
                    detail.save()
                else:
                    # If detail_id is not provided, create a new detail
                    InvoiceDetail.objects.create(invoice=invoice, description=description, quantity=quantity,
                                                 unit_price=unit_price)

            return JsonResponse({'success': True, 'message': f'Invoice {invoice_id} successfully updated'})
        except Invoice.DoesNotExist:
            return JsonResponse({'success': False, 'message': f'Invoice with ID {invoice_id} does not exist'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
