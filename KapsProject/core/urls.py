from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('collections/', views.collections, name='collections'),
    path('kaps_assured/', views.kaps_assured, name='kaps_assured'),
    path('about_us/', views.about_us, name='about_us'),
    path('sell_a_car/', views.sell_a_car, name='sell_a_car'),
    path('happiness_club/', views.HappinessClub_view, name='happiness_club'),
    
    path('contact/', views.contact, name='contact'),
    path('careers/', views.careers, name='career_list'),
    path('proposal/', views.proposal_submission, name='proposal_success'),
    path('find_a_car/', views.find_car, name='find_a_car'),
    path('car_details/', views.car_details, name='car_details'),
    path('emi/', views.emi, name='emi'),
    path('demo_login/', views.demo_login, name='demo_login'),
    
   
    
]
