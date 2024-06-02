from django.db import models

class Category(models.Model):
    name_category = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name_category

class Marka(models.Model):
    name_marka = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name_marka

class Model(models.Model):
    name_model = models.CharField(max_length=32, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_model
        #return f'{self.marka} - {self.name_model}'

class Car(models.Model):
    name_car = models.CharField(max_length=32)
    price = models.PositiveSmallIntegerField(default=1)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    year = models.SmallIntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name_car



