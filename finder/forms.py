from django import forms
from models import Customer

class CustomerForm(forms.ModelForm) :
	class Meta:
		model = Customer
		fields = ['name','Password','Genre1','Genre2','Genre3']


			