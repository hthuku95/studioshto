from django.db import models

# Create your models here.
class About (models.Model):

    name = models.CharField( max_length=50)

    #hto studios components
    htostudios_thumb = models.ImageField()
    htostudios_title = models.CharField( max_length=50)
    htostudios_intro = models.CharField( max_length=256,null=True)
    htostudios_description = models.TextField()

    #harry thuku components
    harry_thumb = models.ImageField()
    harry_title = models.CharField( max_length=50)
    harry_intro = models.CharField( max_length=256,null=True)
    harry_description = models.TextField()


    def __str__(self):
        return self.name



# Components
# @welcome 
class Welcome (models.Model):

    name = models.CharField( max_length=50)

    #welcome page components
    brand_name = models.CharField( max_length=50)
    brand_quote_one = models.CharField( max_length=50)
    brand_quote_two = models.CharField( max_length=50)

    def __str__(self):
        return self.name


# @Services
class Solution (models.Model):

    #service components
    title = models.CharField( max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.title
    