from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    slug = models.SlugField() # for url
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title