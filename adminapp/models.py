from django.db import models

# Create your models here.


class adminLogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    fathername = models.CharField(max_length=50)
    fathermobile = models.BigIntegerField()
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    dob = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    idproof = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    facebookurl = models.CharField(max_length=70)
    twitterurl = models.CharField(max_length=70)
    instagramurl = models.CharField(max_length=70)
    linkedinurl = models.CharField(max_length=70)


class user(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_id = models.ForeignKey(customer, on_delete=models.CASCADE)


class item(models.Model):
    itemname = models.CharField(max_length=100)


class itemtype(models.Model):
    itemtype = models.CharField(max_length=50)


class interest(models.Model):
    interesttype = models.CharField(max_length=50)


class notification(models.Model):
    notify = models.CharField(max_length=500)
