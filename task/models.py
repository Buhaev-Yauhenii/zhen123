from django.db import models



# Create your models here.
class MyModel(models.Model):
    collection = models.JSONField()

    def __str__(self):
        return 'form data in jsonfield'

        
