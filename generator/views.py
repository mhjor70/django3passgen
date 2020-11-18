from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'generator/home.html') 

def about(request):
    return render(request, 'generator/about.html') 

def password(request):
    import random
    thePass = ""
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('UpperCase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('Numbers'):
        characters.extend(list('012345679'))

    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()_+-='))

    passLength = int(request.GET.get('length',12))
    for i in range(0,passLength):
        thePass += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thePass}) 