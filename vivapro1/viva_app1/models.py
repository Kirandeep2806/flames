from django.db import models

# Create your models here.
class Flames(models.Model):
    name1 = models.CharField(max_length=30)
    name2 = models.CharField(max_length=30)
    date = models.DateField()

    def __str__(self):
        return self.name1
    