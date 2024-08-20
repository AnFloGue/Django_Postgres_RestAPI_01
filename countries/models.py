from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    capital = models.CharField(max_length=50, blank=False, default='')
    
    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name