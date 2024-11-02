from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from myapp.models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Custom_User
        fields = ['username', 'email', 'password1', 'password2','user_type']
        
        
        
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Custom_User  
        fields = ['username', 'password']