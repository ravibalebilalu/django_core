from django.db import models
from django.contrib.auth.models import User

class receipe(models.Model):
    user = models.ForeignKey(User,on_delete = models.SET_NULL,null=True,blank=True)
    receipe_name = models.CharField(max_length = 100)
    receipe_decription = models.TextField()
    receipe_image = models.URLField()
    receipe_view_count = models.IntegerField(default = 1)

