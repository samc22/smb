from django.conf.urls import url, include
from django.contrib import admin
from .views import home, addMunicipality


urlpatterns = [
   
    url(r'^$', home, name='home'),
    url(r'^add/$', addMunicipality, name='addMunicipality'),


]