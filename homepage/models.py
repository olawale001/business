from django.db import models


class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    contact = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
