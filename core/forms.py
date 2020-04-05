from django import forms


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
