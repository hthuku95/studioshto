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

 
    introduction = models.TextField(blank=True,null=True)

    thumb_one = models.ImageField(blank=True,null=True)
    thumb_one_description = models.CharField(blank=True, max_length=50)
    section_one = models.TextField()

    thumb_two = models.ImageField(blank=True,null=True)
    thumb_two_description = models.CharField(blank=True, max_length=50)
    section_two = models.TextField(null=True)

    
    thumb_three = models.ImageField(blank=True,null=True)
    thumb_three_description = models.CharField(blank=True, max_length=50)
    section_three = models.TextField(null=True)



    category = models.ManyToManyField(Category,blank = True)

    #snippet utils
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.section_one[:50] 
        
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

#contact model
class Contact (models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    message = models.TextField()

    #snippet utils
    def __str__(self):
        return self.name
