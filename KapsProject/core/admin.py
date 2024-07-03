
from django.contrib import admin
from .models import Car, Career, happiness_club


class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model',  'price', 'is_available', 'transmission', 'inspection_rating', 'reg_year', 'km_driven', 'rto', 'insurance_validity', 'insurance_type', 'no_of_owners', 'finance_available', 'condition')
    search_fields = ('make', 'model', 'reg_year')
    list_filter = ('make', 'reg_year', 'is_available', 'transmission', 'insurance_type', 'condition')


class CareerAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'location', 'date_posted', 'last_date_to_apply')
    search_fields = ('job_title', 'location')
    list_filter = ('location', 'date_posted')
    ordering = ('-date_posted',)

class HappinessClubAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'owner_image')
    search_fields = ['owner_name']  # Corrected to a list
    list_filter = ['owner_name']    # Corrected to a list





admin.site.register(Car, CarAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(happiness_club, HappinessClubAdmin)
