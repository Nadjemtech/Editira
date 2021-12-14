from django.forms import ModelForm
from .models import Client
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name', 'email', 'password1', 'password2',]



class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['phone','address','CCP']


