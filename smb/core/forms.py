from django import forms
from django.forms import ModelForm
from .models import Municipality
from datetime import datetime

class addMunicipalityForm(forms.ModelForm):
	"""
	class Meta:
		model = Municipality
		fields = ('name', 'description', 'states', 'lat', 'log', 'avatar', 'createdDate')
	"""
	name = forms.CharField(label='Name', max_length=200)
	description = forms.CharField(label='Description', widget=forms.Textarea())

	STATES = (
			('Acre', 'AC'), 	 
			('Alagoas', 'AL'), 	 
			('Amapá', 'AP'), 	 
			('Amazonas', 'AM'), 	 
			('Bahia', 'BA'), 	 
			('Ceará', 'CE'),	 
			('Distrito Federal', 'DF'), 	 
			('Espírito Santo', 'ES'), 	 
			('Goiás', 'GO'), 	 
			('Maranhão', 'MA'), 	 
			('Mato Grosso', 'MT'), 	 
			('Mato Grosso do Sul', 'MS'), 	 
			('Minas Gerais', 'MG'), 	 
			('Pará','PA'), 	 
			('Paraíba','PB'), 	 
			('Paraná','PR'), 	 
			('Pernambuco','PE'), 	 
			('Piauí','PI'), 	 
			('Rio de Janeiro','RJ'), 	 
			('Rio Grande do Norte','RN'), 	 
			('Rio Grande do Sul','RS'), 	 
			('Rondônia','RO'), 	 
			('Roraima','RR'), 	 
			('Santa Catarina','SC'), 	 
			('São Paulo','SP'), 	 
			('Sergipe','SE'), 	 
			('Tocantins','TO'),
		)

	states = forms.CharField(max_length=30, widget=forms.Select(choices=STATES))
	lat = forms.CharField(label='Latidude', max_length=10)
	log = forms.CharField(label='Longitude', max_length=10)
	avatar = forms.ImageField(label='Avatar', required=False)

	class Meta:
		model = Municipality
		fields = [
		'name', 
		'description', 
		'states', 
		'lat', 
		'log', 
		'avatar'
		]
class editMunicipalityForm(forms.ModelForm):

	class Meta:
		model = Municipality
		fields = ['name', 'description', 'states', 'lat', 'log', 'avatar']
	
	