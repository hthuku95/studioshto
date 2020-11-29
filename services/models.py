from django.db import models

# Create your models here.

#services
class Service (models.Model):
    name = models.CharField( max_length=50)
    fav_icon = models.CharField(max_length=100)
    description = models.TextField( )

    #snippet utils
    def __str__(self):
        return self.name


#projects
class Project (models.Model):
    thumb = models.ImageField()
    slug = models.SlugField()

    #links
    source_link = models.CharField(default="#",max_length=256)
    display_link = models.CharField(default="#",max_length=256)
    buy_link = models.CharField(default="#",max_length=256)

    #attributes
    title = models.CharField( max_length=100)
    description = models.TextField()
    date = models.DateTimeField( auto_now_add=True)

    #relationships
    service = models.ManyToManyField(Service,blank = True)

    #snippet utils
    def __str__(self):
        return self.title

