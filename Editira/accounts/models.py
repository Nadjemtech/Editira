from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Offer(models.Model):
    offers = (  ('Gold','G'),
                ('Silver','S'),
                ('Branze','B'))
    title       = models.CharField(max_length=50 , choices=offers , blank=True, null=True)
    discount    = models.IntegerField(default=10 )
    description = models.CharField(max_length=100,blank=True, null=True)
    available   = models.DurationField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = 'Offer'
        verbose_name_plural = 'Offers'


class Staff(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    phone       = models.IntegerField(blank=True, null=True)
    address     = models.CharField(max_length=100)
    speciality  = models.CharField(max_length=50)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name        = 'Staff'
        verbose_name_plural = 'Staffs'


class Client(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    phone       = models.IntegerField(blank=True, null=True)
    address     = models.CharField(max_length=100)
    CCP         = models.IntegerField(default=00000000)
    offer       = models.ForeignKey(Offer,null=True , blank= True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


