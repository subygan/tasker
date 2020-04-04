from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProfileForm
from django.shortcuts import render
import datetime
from . import models


def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def registered(request):

    return render(request, 'registered.html', {})

def create_profile(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            profile = models.Profile(**form.cleaned_data)
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            profile.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileForm()

    return render(request, 'signup.html', {'form': form})