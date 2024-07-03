from django.shortcuts import render, redirect
from .forms import CarSellForm
from .models import Career, Car, happiness_club
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'index.html')

def collections(request):
    return render(request, 'collections.html')

def kaps_assured(request):
    return render(request, 'kaps_assured.html')

def about_us(request):
    return render(request, 'about_us.html')

def sell_a_car(request):
    return render(request, 'sell_a_car.html')

def HappinessClub_view(request):
    h_club = happiness_club.objects.all()
    context = {
        'h_club': h_club,
    }
    return render(request, 'happiness_club.html', context)


def contact(request):
    return render(request, 'contact.html')

def sell_a_car(request):
    if request.method == 'POST':
        form = CarSellForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # ...
            pass
    else:
        form = CarSellForm()

    return render(request, 'sell_a_car.html', {'form': form})


#careers views

def careers(request):
    careers = Career.objects.all()
    recent_career = Career.objects.order_by('-date_posted').first()
    recent_email = recent_career.email if recent_career else None
    context = {
        'careers': careers,
        'recent_email': recent_email,
    }

    return render(request, 'careers.html', context)

def proposal_submission(request):
    return render(request, 'proposal_success.html')

def find_car(request):
    return render(request, 'find_car.html')

def car_details(request):
    return render(request, 'car_details.html')

def emi(request):
    return render(request, 'emi.html')


def demo_login(request):
    return render(request, 'otp.html')

