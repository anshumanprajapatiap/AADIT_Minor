from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
# Create your models here.

class user_type(models.Model):
    usertype = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.usertype

class Topics(models.Model):
    topic = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.topic


class departmentincollege(models.Model):
    departmentname = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.departmentname

class proftype(models.Model):
    profdesname = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.profdesname

class user_detail(models.Model):

    usertype = models.ForeignKey(user_type, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    emailaddress = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    image = models.ImageField(null=True, default=None)

    def __str__(self):
        return self.emailaddress

class notice_data(models.Model):
    postuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    usertype = models.ForeignKey(user_type, on_delete=models.CASCADE, null=True)
    noticetile = models.CharField(max_length=100, null=True)
    noticetag = models.ForeignKey(Topics, on_delete=models.CASCADE, null=True)
    noticecontent = models.TextField(null=True)

    def __str__(self):
        return self.usertype.usertype + ' -- ' + self.noticetile

class faculty_general_information(models.Model):
    user = models.ForeignKey(user_detail, on_delete=models.CASCADE, null=True)
    facultyshortdiscription = models.CharField(max_length=300, null=True)
    facultyabout = models.TextField(null=True)

    def __str__(self):
        return self.user.emailaddress


class facultycabinoffice(models.Model):
    collegeidoffaculty = models.ForeignKey(faculty_general_information, on_delete=models.CASCADE, null=True)
    facultyoffice = models.TextField(null=True)

    def __str__(self):
        return self.collegeidoffaculty.user.emailaddress


class About(models.Model):
    databy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body_text = TextField()

    def __str__(self):
        return self.databy.username


class Location(models.Model):
    databy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body_text = TextField()

    def __str__(self):
        return self.databy.username