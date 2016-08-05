from django.conf.urls import url, include
from django.contrib import admin
from .views import home, addMunicipality, editMunicipality, detailMunicipality


urlpatterns = [
   
    url(r'^$', home, name='home'),
    url(r'^add/$', addMunicipality, name='addMunicipality'),
    url(r'^edit/(?P<pk>\d+)/$', editMunicipality, name='editMunicipality'),
    url(r'^detail/(?P<pk>\d+)/$', detailMunicipality, name='detailMunicipality'),

]