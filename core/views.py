from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignupForm
from django.shortcuts import render
import datetime
from . import models


def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def registered(request):

    return render(request, 'registered.html', {})

def Signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid and the confirm password is proper:
        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['confirm_password']:

            profile = models.Profile(**form.cleaned_data)
            profile.save()
            return HttpResponseRedirect('/thanks/')

        elif form.data['password'] != form.data['password_confirm']:
            form.add_error('password_confirm', 'The passwords do not match')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def SignIn(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            profile = models.Profile(**form.cleaned_data)
            profile.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})