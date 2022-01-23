from django.db import models

# Create your models here.

#naming a class always begins with a capital letter
class Project(models.Model):
    #establish a project title with a max character length of 100 characters
    title = models.CharField(max_length=100)
    #gives the project a description with a max character length of 200 characters
    description = models.CharField(max_length=200)
    #if your project has an image, it gets uploaded to portfolio/images/
    image = models.ImageField(upload_to='portfolio/images/')
    #the http address of the project
    url = models.URLField(blank=True)
    
    #returns the name in a more descriptive manner
    def __str__(self):
        return self.title