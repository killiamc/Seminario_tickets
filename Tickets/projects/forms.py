from django import forms
from django.contrib.auth.forms import UserCreationForm
from projects.models import NewUser
from django.contrib.auth import get_user_model

User = get_user_model()

class CreateUserForm(forms.ModelForm):
    
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'required': 'required'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'telefono', 'cedula']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control form-control-lg', 'id': 'first_name', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control form-control-lg', 'id': 'last_name', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control form-control-lg', 'id': 'email', 'required': 'required'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Telefono', 'class': 'form-control form-control-lg', 'id': 'telefono', 'required': 'required'}),
            'cedula': forms.TextInput(attrs={'placeholder': 'Cedula', 'class': 'form-control form-control-lg', 'id': 'cedula', 'required': 'required'}),
        }

class AbonadoForm(forms.Form):
    start = forms.DateField(label='Fecha Inicial', widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'start', 'required': 'required'}))
    end = forms.DateField(label='Fecha Final', widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'end', 'required': 'required'}))
    
    
    




