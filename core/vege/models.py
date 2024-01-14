from django.db import models

class receipe(models.Model):
    receipe_name = models.CharField(max_length = 100)
    receipe_decription = models.TextField()
    receipe_image = models.URLField()

