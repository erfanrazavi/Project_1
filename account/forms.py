from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  



class RegistrationForm(UserCreationForm):
    
    
	"""docstring for RegistrationForm"""
	email = forms.EmailField(required=True)
	


	class Meta: # define a metadata related to this class
		model = User
		fields = (
			'username',
			'email',
			
			'password1',
			'password2',

		)
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		


		if commit:
			user.save() # running sql in database to store data
		return user



