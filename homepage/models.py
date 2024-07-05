from django.db import models


class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
