from django.db import models

# Create your models here.


class CatFacts(models.Model):
    CatFacts = models.CharField(max_length=1000)

    def __str__(self):
        return self.CatFacts