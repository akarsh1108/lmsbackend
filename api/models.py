from django.db import models

# Create your models here.
class Category(models.Model):
    category_id =models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Books(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.CharField(max_length=7)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

