from django import forms
from django.core.validators import RegexValidator

# Define a regular expression pattern that allows only alphabetic characters and spaces
name_validator = RegexValidator(
    r'^[a-zA-Z\s]*$',
    'Only alphabetic characters and spaces are allowed.'
)

class NewUserForm(forms.Form):
    # CharField for first name with maximum length of 140 characters
    first_name = forms.CharField(
        min_length=2, max_length=140, validators=[name_validator],
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text="Enter your first name ( Not blank maximum 140 characters). No special characters allowed."
    )

    # CharField for username with maximum length of 140 characters
    username = forms.CharField(
        min_length=2, max_length=140, validators=[name_validator],
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text="Enter your username ( Not blank maximum 140 characters). No special characters allowed."
    )

    # CharField for password1 with widget set as PasswordInput (to hide input)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,
        help_text="Enter your password (minimum 8 characters)"
    )

    # CharField for password confirmation with widget set as PasswordInput (to hide input)
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,
        help_text="Confirm your password (minimum 8 characters)"
    )