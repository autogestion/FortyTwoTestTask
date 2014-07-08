
from django.shortcuts import render
from .models import Contact

def home(request):
    user = Contact.objects.all()[0]
    return render(request, 'hello/home.html', {'user': user})
