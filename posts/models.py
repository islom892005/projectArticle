from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.urls import reverse



class Content(models.Model):
    
    title = models.CharField(max_length=255)
    picture_of_content = models.ImageField(upload_to="Content/photos/%Y/%m/%d/", default="Content\photos\default.png")
    text_of_content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Har turdagi maqolalar"
        verbose_name_plural = "Har turdagi maqolalar"
        ordering = ['time_create', 'title']



class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    picture_of_Category = models.ImageField(upload_to="Category/photos/%Y/%m/%d", default=None)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_posts', kwargs={'category_slug':self.slug})
    class Meta:
        verbose_name = "Maqola turlari"
        verbose_name_plural = "Maqola turlari"
        ordering = ['name']

# class Person(models.Model):
    
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
#     bio = models.TextField(null=True)
    
     
#     picture_of_Person = models.ImageField(upload_to="person/photos/%Y/%m/%d/", default=None)
#     name_of_blog = models.CharField(max_length=255)

#     def __str__(self):
#         return self.user.username