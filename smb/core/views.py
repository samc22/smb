from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from smb.core.models import Municipality
from .forms import addMunicipalityForm, editMunicipalityForm
# Create your views here.

def home(request):
	"""
	
	"""
	context = {
		'municipalities': Municipality.objects.all().order_by('-createdDate')
	}

	return render(request, 'core/municipality.html', context)


def addMunicipality(request):
	if request.method == 'POST':
		form = addMunicipalityForm(request.POST or None, request.FILES or None)
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
	form = editMunicipalityForm(request.POST or None, request.FILES or None, instance=instance)
	#print(form)
	print(instance.avatar)
	if instance:
		if form.is_valid():
			print(form)
			form.save()
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

def deleteMunicipality(request, pk):
	
	instance = get_object_or_404(Municipality, pk=pk)
	instance.delete()
	return redirect('/municipality/list')

def listMunicipality(request):

	municipalities = Municipality.objects.all().order_by('-createdDate')

	context = {

		'municipalities': municipalities
	}

	return render(request, 'core/listMunicipality.html', context)
