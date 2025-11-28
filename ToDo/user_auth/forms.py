from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    full_name = forms.CharField(max_length=150, required=True)
    contact_no = forms.CharField(max_length=20, required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'contact_no', 'password', 'password2']

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Passwords do not match')
        return cleaned

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ForgotPasswordForm(forms.Form):
    username = forms.CharField()
    new_password = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')
    def clean(self):
        cd = super().clean()
        if cd.get('new_password') != cd.get('new_password2'):
            raise forms.ValidationError('Passwords do not match')
        return cd

class EditProfileForm(forms.ModelForm):
    full_name = forms.CharField(max_length=150, required=False)
    contact_no = forms.CharField(max_length=20, required=False)
    class Meta:
        model = User
        fields = ['username', 'email']
