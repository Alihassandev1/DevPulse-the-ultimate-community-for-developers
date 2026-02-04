from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        required=True, 
        max_length=100, 
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-glass required'}
            )
        )
    last_name = forms.CharField(
        required=True, 
        max_length=100, 
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-glass required'}
            )
        )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(
            attrs={'class': 'form-control form-control-glass required'}
            )
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user