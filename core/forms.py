from django import forms
from .models import Task
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class SignupForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    # Still am guilty about this
    password = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='confirm password', max_length=50, widget=forms.PasswordInput)
    first_name = forms.CharField(label='first name of the user', max_length=50)
    last_name = forms.CharField(label='last name', max_length=50)
    bio = forms.CharField(max_length=200)


class SigninForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput)


class CreateTaskForm(forms.Form):
    """
        form to create task
    """
    title = forms.CharField(help_text='Task Title',)
    description = forms.CharField(help_text='Task description')
    start_time = forms.DateTimeField(widget=forms.SelectDateWidget(),help_text='Start time of task')
    completion_time = forms.DateTimeField(widget=forms.SelectDateWidget(),help_text='completion time')
    
    # def clean_renewal_date(self):
    #     """
    #
    #     :return:
    #     """
    #     data = self.cleaned_data['renewal_date']
    #
    #     # Check if a date is not in the past.
    #     if data < datetime.date.today():
    #         raise ValidationError(_('Invalid date - renewal in past'))
    #
    #     # Check if a date is in the allowed range (+4 weeks from today).
    #     if data > datetime.date.today() + datetime.timedelta(weeks=4):
    #         raise ValidationError(
    #             _('Invalid date - renewal more than 4 weeks ahead'))
    #
    #     # Remember to always return the cleaned data.
    #     return data
