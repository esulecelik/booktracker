from typing import Iterable
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.text import slugify
from datetime import datetime
# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50)


class Writer(models.Model):
    
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)


class Book(models.Model):
    
    name = models.CharField(max_length=70)
    writer = models.ForeignKey(Writer,on_delete=models.CASCADE,null=True)
    page_number = models.IntegerField(validators=[ MinValueValidator(1)])
    current_page = models.IntegerField(default=0)
    started_on = models.DateTimeField(null=True)
    finished_on = models.DateTimeField(null=True)
    created_on = models.DateTimeField(null=True,auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="covers/",null=True,blank=True)
    slug = models.SlugField(default="",blank=True)

    def progress(self):
        read_pages = self.current_page
        progress = (read_pages / self.page_number) * 100
        return int(progress)
    
    def save(self, *args, **kwargs) -> None:

        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)


class Quote(models.Model):

    book = models.ForeignKey(Book, on_delete= models.CASCADE)
    page_number = models.IntegerField(null=True, validators=[ MinValueValidator(1)])
    text = models.TextField(default="")
