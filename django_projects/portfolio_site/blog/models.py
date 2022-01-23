from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    date = models.DateField()
    
    def _str_(self):
        return self.title