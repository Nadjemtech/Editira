from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Offer(models.Model):
    offers = (('Gold', 'G'),
              ('Silver', 'S'),
              ('Branze', 'B'))
    title = models.CharField(
        max_length=50, choices=offers, blank=True, null=True)
    discount = models.IntegerField(default=10)
    started  = models.DateField(auto_now=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    available = models.DurationField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100)
    speciality = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100)
    CCP = models.IntegerField(default=00000000)
    offer = models.ForeignKey(
        Offer, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class notification(models.Model):
    """Model definition for notification."""

    content = models.CharField(max_length=500)
    staff = models.ForeignKey(
        Staff, blank=True, null=True, on_delete=models.SET_NULL)
    client = models.ForeignKey(
        Client, blank=True, null=True, on_delete=models.SET_NULL)
    checked = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for notification."""

        verbose_name = 'notification'
        verbose_name_plural = 'notifications'

    def __str__(self):
        """Unicode representation of notification."""
        return "Notification"
