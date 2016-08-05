from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from smb.core.models import Municipality
from .forms import addMunicipalityForm, editMunicipalityForm
# Create your views here.

def home(request):

	context = {
		'municipalities': listMunicipality()
	}

	return render(request, 'core/municipality.html', context)


def addMunicipality(request):
	if request.method == 'POST':
		form = addMunicipalityForm(request.POST)
		if form.is_valid():
			print(form)
			form.save()
			return redirect('/municipality')
	else:
		form = addMunicipalityForm()
	context = {

		'form': form
	}
	return render(request, 'core/addMunicipality.html', context)

def editMunicipality(request, pk):
	instance = get_object_or_404(Municipality, pk=pk)
	form = editMunicipalityForm(request.POST or None, instance=instance)
	print(form)
	if instance:
		if form.is_valid():
			print(form)
			form.save(commit=False)
			return redirect('/municipality')
	else:
		form = addMunicipalityForm()
	context = {

		'form': form
	}
	return render(request, 'core/editMunicipality.html', context)



def detailMunicipality(request, pk):
	municipality = get_object_or_404(Municipality, pk=pk)
	context = {
		'municipality': municipality
	}
	return render(request, 'core/detailMunicipality.html', context)	

def deleteMunicipality(request):

	pass


def listMunicipality():

	municipalities = Municipality.objects.all().order_by('-createdDate')

	return municipalities
