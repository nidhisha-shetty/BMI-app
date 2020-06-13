from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class BMI(models.Model):
	height=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default="1");
	weight=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default="1");
	
