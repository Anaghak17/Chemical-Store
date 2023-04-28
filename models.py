from django.db import models
from c_app.models import*
# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=30)
    password=models.IntegerField()
    email=models.EmailField()
    phone=models.IntegerField()
    def __str__(self):
        return self.name
class Cart(models.Model):
      userid  =  models.ForeignKey(Register, null=True, on_delete=models.CASCADE)
      productid = models.ForeignKey(chemical,null=True,on_delete=models.CASCADE)
      status =models.IntegerField()
      total=models.IntegerField()
      quantity=models.IntegerField()
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=50)
class Checkout(models.Model):
    userid  =  models.ForeignKey(Register, null=True, on_delete=models.CASCADE)
    cartid  =  models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    address =  models.CharField(max_length=30)
    state   =  models.CharField(max_length=30,default="")
    country =  models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    postal_zip = models.CharField(max_length=30)
