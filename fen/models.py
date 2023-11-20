from django.db import models
import decimal


# Create your models here.
class Receipt(models.Model):
    restaurant_name = models.CharField(max_length=200)
    total_people = models.IntegerField(default=0)

    def __str__(self):
        return self.restaurant_name


class Item(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    num_split = models.IntegerField(default=0)

    @property
    def split_cost(self):
        split_cost = round(self.price / self.num_split, 2)
        return split_cost

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=200)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
