from django.shortcuts import render, HttpResponse
from smb.core.models import Municipality

# Create your views here.

def home(request):

	return render(request, 'core/municipality.html')