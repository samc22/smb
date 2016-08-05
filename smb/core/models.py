from django.db import models

#from django.contrib.auth.models import User
# Create your models here.


class Municipality(models.Model):


	name = models.CharField(max_length=200)
	description = models.TextField()
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
	states = models.CharField(max_length=30, choices=STATES)
	lat = models.CharField(max_length=10)
	log = models.CharField(max_length=10)
	avatar = models.ImageField(upload_to='avatar/', blank=True)
	createdDate = models.DateTimeField(auto_now_add=True, blank=True)
	#user = models.ForeignKey(User)
		
	def __str__(self):

		return self.name
