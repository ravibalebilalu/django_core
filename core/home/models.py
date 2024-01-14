from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField(null = True,blank = True)
    adress = models.TextField()
     
     
    """def __str__(self):
        return self.name

    def __str__(self):
        return self.age
    def __str__(self):
        return self.email
    def __str__(self):
        return self.adress"""


class Car(models.Model):
    car_name = models.CharField(max_length= 100)
    speed = models.IntegerField(default = 50)

    def __str__(self):
        return self.car_name

      
      