from django.db import models

# Create your models here.


# class Blog(models.Model):
#     title = models.CharField(max_length=120)
#     date = models.DateField(auto_now=False, auto_now_add=False)
#     summary = models.TextField(blank=False, null=False)

class Post(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title
