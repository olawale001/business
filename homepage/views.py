from django.shortcuts import render
# from .models import PersonalInfo

def home(request):
    context = {
        'name': 'Lateef',
        'bio': 'I am softwear Engineer and am work at apple and tiktok',
        'contact': 'You can reach me through social media and my website',
    }

    return render(request, 'home.html', {'context': context})