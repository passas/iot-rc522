from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    _roles = (
        ('Super', 'Super'),
        ('Agent', 'Agent'),
        ('Sensor', 'Sensor'),
        ('Client', 'Client'),
    )
    role = models.CharField(max_length=16, choices=_roles, default='Client')
    card_id = models.CharField(max_length=16, unique=True)
    
    def __str__(self):
        return f'{self.id} {self.username} {self.role}'
    
    def getTicket(self):
        #return Ticket.objects.get(card_id=self.card_id)
        return Ticket.objects.filter(card_id=self.card_id).last()

class Contract(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    type = models.CharField(max_length=16, default=16*'#')
    zone1 = models.CharField(max_length=16, default=16*'#')
    zone2 = models.CharField(max_length=16, default=16*'#')
    price = models.CharField(max_length=16, default=16*'#')
    expire = models.CharField(max_length=16, default=16*'#')
    until = models.CharField(max_length=16, default=16*'#')
    zone = models.CharField(max_length=16, default=16*'#')
    date = models.CharField(max_length=16, default=16*'#')

    def __str__(self):
        return f'{self.type} {self.zone1} {self.zone2} {self.price}'
    
class Ticket(models.Model):
    card_id = models.CharField(max_length=16, default=16*'#')
    type = models.CharField(max_length=16, default=16*'#')
    zone1 = models.CharField(max_length=16, default=16*'#')
    zone2 = models.CharField(max_length=16, default=16*'#')
    amount = models.CharField(max_length=16, default=16*'#')
    zone = models.CharField(max_length=16, default=16*'#')
    date = models.CharField(max_length=16, default=16*'#')

    def __str__(self):
        return f'{self.type} {self.zone1} {self.zone2} {self.amount}'
    
class Train(models.Model):
    def __str__(self):
        return f'{self.id}'

class TemperatureHumidity(models.Model):
    train = models.ForeignKey('Train', on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.CharField(max_length=22) #YYYY-mm-dd hh:mm:ss

    def __str__(self):
        return f'{self.train_id} {self.temperature}ºC {self.humidity}% {self.timestamp}'
