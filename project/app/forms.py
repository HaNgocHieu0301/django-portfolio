"""
    A module to define the form model for the different forms in project
"""
from django.forms import ModelForm
from .models import Contact
from django import forms


# class ContactForm(forms.Form):
#     """
#         A class form for fill and submit contact form
#     """
#     name = forms.CharField(label='name', max_length=200)
#     email = forms.EmailField(label='email')
#     message = forms.CharField(label='message')

class ContactForm(ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


# class UserForm(ModelForm):
#     class Meta:
#         model = UserInfo
#         fields = ['username', 'password']
#
#     def save(self, commit=True, *args, **kwargs):
#         m = super().save(commit=False)
#         m.password = make_password(self.cleaned_data.get('password'))
#         m.username = self.cleaned_data.get('username').lower()
#         if commit:
#             m.save()
#         return m
#
#
# class UserDetailsForm(ModelForm):
#     last_name = forms.CharField(required=False)
#
#     class Meta:
#         model = UserInfo
#         fields = ['first_name', 'last_name', 'email', 'address', 'phone']
#
#
# """
#     def clean_phone(self):
#         phone = self.cleaned_data.get('phone')
#         if len(phone) < 10:
#             raise forms.ValidationError("Phone needs to be of length 10 characters")
#         return phone
# """
