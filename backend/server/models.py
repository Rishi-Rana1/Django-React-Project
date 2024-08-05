from django.db import models

class Macronutrients(models.Model):
    calories = models.IntegerField()
    carbohydrates = models.IntegerField()
    fats = models.IntegerField()
    proteins = models.IntegerField()
    fiber = models.IntegerField()
    water = models.IntegerField()

    def __str__(self):
        return f"{self.calories} {self.carbohydrates} {self.fats} {self.proteins} {self.fiber} {self.water}"
    
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    macros = models.ForeignKey(Macronutrients, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.age} {self.weight} {self.height}"

class TestModel(models.Model):
    thing = models.CharField(max_length=100)

    def __str__(self):
        return self.thing