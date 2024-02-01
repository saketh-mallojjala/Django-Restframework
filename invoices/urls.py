from django.urls import path
from .views import AddInvoiceView, ViewInvoiceView, DeleteInvoiceView, UpdateInvoiceView

urlpatterns = [
    path('addinvoice/', AddInvoiceView.as_view(), name='add_invoice'),
    path('viewinvoice/', ViewInvoiceView.as_view(), name='view_invoice'),
    path('deleteinvoice/<int:invoice_id>/', DeleteInvoiceView.as_view(), name='delete_invoice'),
    path('updateinvoice/<int:invoice_id>/', UpdateInvoiceView.as_view(), name='update_invoice'),
]
