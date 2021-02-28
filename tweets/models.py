from django.db import models

# Create your models here.
class Tweet(models.Model):
    # id is a automatic field , which will be the default primary key
    content = models.TextField()
    image = models.FileField(upload_to='images/',blank=True, null=True)
    def __str__(self):
        return self.content
