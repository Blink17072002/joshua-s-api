from django.db import models

# Create your models here.
class Models(models.Model):
    name = models.CharField(max_length=250, null=True)
    year = models.IntegerField()
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name