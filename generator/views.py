from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def Home(request):

    return render(request, 'generator/home.html')


def About(request):

    return render(request, 'generator/about.html')


def Password(request):

    characters = list('abcdefghijklmnopqrstuvwsyz')
    upperCase = request.GET.get('uppercase')
    specialChar = request.GET.get('special')
    numbers = request.GET.get('numbers')

    if upperCase:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWSYZ'))
    if specialChar:
        characters.extend(list('"#$%&()*+,-./:;< [\]^_`|!@'))
    if numbers:
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 14))
    thePassword = ''

    for x in range(length):
        thePassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thePassword})
