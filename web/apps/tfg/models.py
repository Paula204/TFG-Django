from django.db import models

# Create your models here.

class News(models.Model):
    id = models.AutoField(primary_key=True)
    fechaEntrada = models.DateField('Fecha de creación', auto_now=True, auto_now_add=False)
    url = models.URLField(blank=False, null=False)
    esFi = models.BooleanField(null=False, default=False)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['fechaEntrada']

    def __str__(self):
        return self.url





