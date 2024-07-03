from django.shortcuts import render
from django.http import HttpResponse

def billing_view(request):
  return HttpResponse("<h1>billing</h1>")
  