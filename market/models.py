from django.db import models

# Create your models here.

class Type(models.Model):
    Type = models.CharField(max_length = 100)
    YM = models.IntegerField(default = 0)
    BAS_ID = models.CharField(max_length = 10)
    totalspent = models.IntegerField(default = 0)
    Disspent = models.IntegerField(default = 0)
    Numofspent = models.IntegerField(default = 0)
    NumofDisspent = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.s_name
