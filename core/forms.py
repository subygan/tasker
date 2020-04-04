from django import forms


class ProfileForm(forms.Form):
    username = forms.CharField(label='username of the user', max_length=50)
    # Still am guilty about this
    password = forms.CharField(label='password of the user', max_length=50, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='confirm password of the user', max_length=50, widget=forms.PasswordInput)
    first_name = forms.CharField(label='first name of the user', max_length=50)
    last_name = forms.CharField(label='last name', max_length=50)
    bio = forms.CharField(max_length=200)
