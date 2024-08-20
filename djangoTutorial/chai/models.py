from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    # This is an Enum : Enums represents a collection of constants that are grouped together under a single name
    CHAI_TYPE_CHOICE = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('CH','CHOCOLATE'),
        ('EL','PLAINCHAI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added =  models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name
