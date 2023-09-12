from django import forms
from napp.models import Employee
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields='__all__'

class SignUpForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','password','email','first_name','last_name']