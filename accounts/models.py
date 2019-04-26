from django.db import models
from django.conf import settings
import datetime

SPECIALITY_CHOICES = (
    ('dermetalogy','dermetalogy'),
    ('Cardiology', 'Cardiology'),
    ('ENT','ENT'),
    ('oncology','oncology'),
    ('neurology','neurology'),
    ('pediatrics','pediatrics'),
    ('gynecology','gynecology'),
)

GENDER_CHOICES = (('M','Male'),('F','Female'))
APP_CHOICES = (('first','First Visit'),('follow_up','Follow up'))
class Appointment(models.Model):
	Name = models.CharField(max_length = 50)
	Gender = models.CharField(choices = GENDER_CHOICES,max_length = 128,default = 'M')
	dob = models.DateField(max_length = 8)
	age = models.IntegerField()
	
	phone = models.CharField(max_length= 12)
	Email = models.EmailField(max_length = 70,blank = True)
	Speciality = models.CharField(choices = SPECIALITY_CHOICES,max_length = 128)
	Appointment_catogory = models.CharField(choices = APP_CHOICES,max_length = 128,default = 'first')
