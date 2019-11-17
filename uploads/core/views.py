from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

import csv
import pandas as pd

def stronaglowna(request):
    print('stronaglowna')
    return render(request, 'stronaglowna.html')

def pizza(request):
    print('pizza')
    return render(request, 'pizza.html')

def burgery(request):
    print('burgery')
    return render(request, 'burgery.html')

def kebab(request):
    print('kebab')
    return render(request, 'kebab.html')

def tajskie(request):
    print('tajskie')
    return render(request, 'tajskie.html')

def wege(request):
    print('wege')
    return render(request, 'wege.html')

def sushi(request):
    print('sushi')
    return render(request, 'sushi.html')
