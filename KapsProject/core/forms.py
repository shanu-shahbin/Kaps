from django import forms
# from .models import Application

class CarSellForm(forms.Form):
    registration_number = forms.CharField(label='Your Car Registration Number', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Car Registration number'}))
    brand = forms.ChoiceField(label='Select Brand', choices=[('brand1', 'Brand 1'), ('brand2', 'Brand 2')])
    model = forms.ChoiceField(label='Select Model', choices=[('model1', 'Model 1'), ('model2', 'Model 2')])
    registered_year = forms.IntegerField(label='Registered Year', widget=forms.NumberInput(attrs={'placeholder': 'Registered year'}))
    fuel_type = forms.ChoiceField(label='Fuel Type', choices=[('petrol', 'Petrol'), ('diesel', 'Diesel')])
    km_driven = forms.IntegerField(label='KM Driven', widget=forms.NumberInput(attrs={'placeholder': 'KM Driven'}))
    expected_price = forms.DecimalField(label='Expected Price', max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'placeholder': 'Expected price'}))


