from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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


# One to many
# When we use foreign key then it automatically detects that it is one to many relationship
class ChaiReview(models.Model):
    # Inside chai field I have passed chaiVariety model 
    chai = models.ForeignKey(ChaiVariety,on_delete=models.CASCADE , related_name='reviews') #related name means , what this should be called in another table
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'


# Many to Many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety,related_name='stores')

    def __str__(self):
        return self.name

#One to one 
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length = 100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.chai}'
