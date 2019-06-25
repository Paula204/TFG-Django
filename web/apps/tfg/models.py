from django.db import models

# Create your models here.

class News(models.Model):
    id = models.AutoField(primary_key= True)
    fechaEntrada = models.DateField('Fecha de creación', auto_now= True, auto_now_add= False)
    url = models.CharField(max_length=2000, blank= False, null= False)
    esFi =  models.BooleanField(null= False, default= False)

    def __str__(self):
        return self.url





