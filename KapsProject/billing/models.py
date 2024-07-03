from django.db import models

class Billing(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=15, verbose_name='Phone Number')
    gst = models.CharField(max_length=15, verbose_name='GST Number')
    gst_amount = models.DecimalField(max_digits=10, decimal_places=2, null= True, blank= True,verbose_name='GST Amount')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')
    total_bill = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total Bill')

    def __str__(self):
        return f"{self.name} - {self.total_bill}"
    
    class Meta:
        verbose_name = 'Billing'
        verbose_name_plural = 'Billings'
