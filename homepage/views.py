from django.shortcuts import render
from .models import PersonalInfo

def home(request):
    info = PersonalInfo.objects.first()
    return render(request, 'homepage/home.html', {'info':info})
