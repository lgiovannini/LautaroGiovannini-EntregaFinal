from django.db import models

class Ropa(models.Model):
    type = models.CharField(max_length=15)
    brand = models.CharField(max_length=15)
    size = models.CharField(max_length=15)
    
    def __str__(self):
        return f'{self.type} {self.brand} {self.size}'