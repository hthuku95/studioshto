from django.contrib import admin
from .models import Contact ,Article,Comment,Category,Reply,Author,Section,Shape
# Register your models here.
admin.site.register(Contact)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Section)
admin.site.register(Shape)