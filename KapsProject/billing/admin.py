from django.contrib import admin
from .models import Billing

class BillingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'gst', 'amount', 'total_bill', 'gst_amount')
    search_fields = ('name', 'email', 'phone_number', 'gst')
    list_filter = ('name', 'gst', 'gst_amount')

admin.site.register(Billing, BillingAdmin)
