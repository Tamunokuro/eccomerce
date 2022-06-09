from cProfile import label
from dataclasses import field
from xml.dom import ValidationErr
from django import forms
from .models import UserBase
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordResetForm, SetPasswordForm)


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(
        label='Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(label='Email', help_text='Required', error_messages={
        'required': 'Sorry!, you need an email address'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exist")
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cd['password2']

    def cleaned_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'An account has been registered with this email already'
            )
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-user'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Password',
        'id': 'login-pwd'
    }))


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label='Account Email (can not be changed)', max_length=265, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Email',
        'id': 'form-email',
        'readonly': 'readonly'}
    ))

    first_name = forms.CharField(label='First Name', max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'First Name',
        'id': 'form-firstname',
    }))

    last_name = forms.CharField(label='Last Name', max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Last Name',
        'id': 'form-lastname'
    }))

    address1 = forms.CharField(label='Address', max_length=265, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Address',
        'id': 'form-address'
    }))

    phone_number = forms.CharField(label='Phone Number', max_length=265, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Phone Number',
        'id': 'form-phone_number'
    }))

    towncity = forms.CharField(label='City', max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'City',
        'id': 'form-city'
    }))

    class Meta:
        model = UserBase
        fields = ('email', 'first_name', 'last_name',
                  'address1', 'phone_number', 'towncity',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['address1'].required = True
        self.fields['phone_number'].required = True
        self.fields['towncity'].required = True


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=240, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3',
               'placeholder': 'Email', 'id': 'form-email'}
    ))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Email Address not found'
            )
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'New Password',
        'id': 'form-newpass'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Confirm Password',
            'id': 'form-newpass2'}
    ))
