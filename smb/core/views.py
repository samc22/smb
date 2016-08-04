from django.shortcuts import render, HttpResponse
from smb.core.models import Municipality
from .forms import addMunicipalityForm
# Create your views here.

def home(request):

	context = {
		'municipalities': listMunicipality()
	}

	return render(request, 'core/municipality.html', context)


def addMunicipality(request):
	if request.method == 'POST':
		form = addMunicipalityForm(request.POST)
	else:
		form = addMunicipalityForm()
	context = {

		'form': form
	}
	return render(request, 'core/addMunicipality.html', context)

def editMunicipality(request):

	pass



def deleteMunicipality(request):

	pass


def listMunicipality():

	municipalities = Municipality.objects.all().order_by('-createdDate')

	return municipalities
