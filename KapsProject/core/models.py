

from django.db import models

class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
        ('semi-automatic', 'Semi-Automatic'),
    ]

    INSURANCE_TYPE_CHOICES = [
        ('comprehensive', 'Comprehensive'),
        ('third-party', 'Third Party'),
        ('own-damage', 'Own Damage'),
    ]

    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
    ]

    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES, default='manual')
    inspection_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    reg_year = models.IntegerField()
    km_driven = models.IntegerField()
    rto = models.CharField(max_length=100)
    insurance_validity = models.DateField()
    insurance_type = models.CharField(max_length=20, choices=INSURANCE_TYPE_CHOICES, default='comprehensive')
    no_of_owners = models.IntegerField()
    finance_available = models.BooleanField(default=False)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='used')

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"




# careers


class Career(models.Model):
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    date_posted = models.DateField(auto_now_add=True)
    last_date_to_apply = models.DateField()

    def __str__(self):
        return self.job_title

class happiness_club(models.Model):
    owner_name = models.CharField(max_length=100)
    owner_image = models.ImageField(upload_to='happiness_club/', blank=True,)
    owner_info = models.CharField(max_length=100)
    testimonial = models.CharField(max_length=200)

    def __str__(self):
        return self.owner_name