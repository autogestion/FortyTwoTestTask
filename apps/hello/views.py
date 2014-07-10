
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
import json

from .models import Contact, HttpRequestList
from .forms import info_form, PriorityForm


def home(request):
    user_info = Contact.objects.get(id=1)
    return render(request, 'hello/home.html' ,
        {'user_info': user_info})


def requestList(request):
    form = PriorityForm(request.GET or None)
    data = HttpRequestList.objects.all()
    if request.method == 'GET':
        if form.is_valid():
            priority = form.cleaned_data.get('priority', 1)
            data = data.filter(priority=priority)

    return render(request, 'hello/requests.html',
        {'requests': data[:10], 'form': form})



@login_required
def edit_page(request):
    info = get_object_or_404(Contact, pk=1)
    form = info_form(request.POST or None, request.FILES or None,
        instance=info)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return HttpResponse(json.dumps({"success": "saved"}),
                        content_type="application/json")
            else:
                return HttpResponseRedirect(reverse('home'))
        elif request.is_ajax():
                errors_dict = {}
                if form.errors:
                    for error in form.errors:
                        e = form.errors[error]
                        errors_dict[error] = unicode(e)
                    return HttpResponseBadRequest(json.dumps(errors_dict),
                                        content_type="application/json")

    return render(request, 'hello/edit.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))







