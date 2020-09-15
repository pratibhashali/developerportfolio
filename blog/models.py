from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length = 100)
    blog_author = models.CharField(max_length = 100)
    blog_date = models.DateField()
    blog_description = models.TextField()
    blog_image = models.ImageField(upload_to='images/') # Blog images
