from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

    def __str__(self):
        return str(self.firstName, self.lastName)
        
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
   
   
    
