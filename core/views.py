from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignupForm, SigninForm, CreateTaskForm
from django.shortcuts import render
import datetime
from . import models
from .models import Task, Profile
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse


def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def registered(request):

    return render(request, 'registered.html', {})


def sign_up(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid and the confirm password is proper:
        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['confirm_password']:

            user_data = form.cleaned_data
            profile = models.Profile(username=user_data['username'],
                                     password=user_data['password'],
                                     first_name=user_data['first_name'],
                                     last_name=user_data['last_name'],
                                     bio=user_data['username']
            )
            profile.save()
            return HttpResponseRedirect('/thanks/')

        elif form.data['password'] != form.data['password_confirm']:
            form.add_error('password_confirm', 'The passwords do not match')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def sign_in(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SigninForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                user = models.Profile.objects.get(username=form.cleaned_data['username'])
                user_data = user.get_data()

            except ObjectDoesNotExist:

                form.add_error('username', 'the username is not found')
                return HttpResponseRedirect('/sign_in/')

            if form.cleaned_data['password'] == user.get_password():

                request.session['profile'] = user_data

                return HttpResponseRedirect('/profile/')

            else:
                form.add_error('password', 'password is not as expected')

            print("i")
            
            return HttpResponseRedirect('/profile/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SigninForm()

    return render(request, 'signin.html', {'form': form})


def profile(request):
    print("ru", request.user)
    if request.session:
        print('<<<=====>>>')
        user_data = request.session['profile']
        return render(request, 'profile.html', user_data)
    else:
        return HttpResponseRedirect('/profile/')


def create_task(request):
    """
    view to create task
    :param request:
    :return:
    """
    print("ru", request.user)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            user_data = request.session['profile']
            user = Profile.objects.get(username = user_data['username'])
            task = Task.objects.create(user = user,
                                       title = form.cleaned_data['title'],
                                       description = form.cleaned_data['description'],
                                       start_time = form.cleaned_data['start_time'],
                                       completion_time = form.cleaned_data['completion_time']
                                       )
            # task = form.save(commit  =false)
            task.save()
        
            return HttpResponseRedirect(reverse('profile'))
    else:
        
        form = CreateTaskForm()

    context = {
        'form': form,
    }

    return render(request, 'create_task_form.html', context)
