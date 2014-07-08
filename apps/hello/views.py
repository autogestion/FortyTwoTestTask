
from django.shortcuts import render
from .models import Contact, HttpRequestList

def home(request):
    user = Contact.objects.all()[0]
    return render(request, 'hello/home.html', {'user': user})


def requestList(request):
    return render(request, 'hello/requests.html', {'requests': HttpRequestList.objects.order_by('-date')[:10]})
