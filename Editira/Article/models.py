from django.db import models
from django.db.models.fields import CharField
from accounts.models import Staff , Client



# Create your models here.
class Service(models.Model):
    title       = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    tarif       =models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Servece'
        verbose_name_plural = 'Serveces'        


class Artical(models.Model):
    states = (  ('submitted','Submitted'),
                ('delivered','Delivered'),
                ('accepted','Accepted'),
                ('rejected','Rejected'))
    
    
    service = models.ManyToManyField(Service)
    description = models.CharField(max_length=500)
    staff       = models.ForeignKey(Staff, null=True,on_delete=models.SET_NULL)
    client      = models.ForeignKey(Client, null=True,on_delete=models.SET_NULL)
    stat        = models.CharField(max_length=50,choices=states)
    price       = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Artical'
        verbose_name_plural = 'Articals'


