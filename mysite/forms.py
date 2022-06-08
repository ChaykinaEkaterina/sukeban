from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    username = forms.CharField(label='Username', max_length=20, min_length=5, widget = forms.TextInput)
    email = forms.CharField(label='Email', widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, min_length=5, widget = forms.TextInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class CommentForm(forms.Form):
    text = forms.CharField(label='Text', max_length=300, widget = forms.TextInput)