from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

#category model
class Category (models.Model):
    name = models.CharField( max_length=50)
    thumb = models.ImageField()

    def __str__(self):
        return self.name

#author model
class Author (models.Model):
    name = models.CharField( max_length=50)
    profile = models.ImageField()
    twitter = models.CharField( max_length=100)

    #snippet utils
    def __str__(self):
        return self.name

#article model
class Article (models.Model):
    title = models.CharField( max_length=50 ,blank=True)
    slug = models.SlugField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(  auto_now_add=True)
    summary = models.CharField( max_length=100)
    views = models.IntegerField(blank=True,default=0,null=True)

    thumb = models.ImageField()
    thumb_description = models.CharField( max_length=50,null=True) 

    category = models.ManyToManyField(Category,blank = True)

    #snippet utils
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.summary[:50] 
        
#comment model
User = get_user_model()
class Comment (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    parent_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateTimeField(  auto_now_add=True,blank=True,null=True)
    comment_body = models.TextField( max_length=100)

    #snippet utils
    def __str__(self):
        return self.comment_body[:40]

#reply model
class Reply (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    parent_comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    date = models.DateTimeField(  auto_now_add=True,blank=True,null=True)
    reply_body = models.TextField(max_length=100)

    #snippet utils
    def __str__(self):
        return self.reply_body[:40]

# @Types model
class Shape (models.Model):
    name = models.CharField( max_length=50)
    date = models.DateTimeField(  auto_now_add=True,blank=True,null=True)

    #snippet utils
    def __str__(self):
        return self.name

# @sections model
class Section (models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    section_id = models.AutoField(primary_key=True)
    section_shape = models.ForeignKey(Shape,blank=True,null=True ,on_delete=models.CASCADE)
    heading = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True)
    paragraph = models.TextField(blank=True)
    code = models.TextField(blank=True)
    code_language = models.CharField(null=True,blank=True, max_length=50)
    video = models.FileField(blank=True)


    #snippet utils
    def __str__(self):
        return self.paragraph[:20]
    
#contact model
class Contact (models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    message = models.TextField()

    #snippet utils
    def __str__(self):
        return self.name
