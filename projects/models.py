from django.db import models


class Experience(models.Model):
    companyName = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    fromDate = models.CharField(max_length=10)
    toDate = models.CharField(max_length=10)
    description = models.TextField()
    technology = models.TextField()
    image = models.FilePathField(path="/img")


class AboutMe(models.Model):
    about = models.TextField()
    title = models.CharField(max_length=100)
    dob = models.CharField(max_length=10)
    phone = models.CharField(max_length=13)
    age = models.IntegerField()
    location = models.TextField()
    email = models.EmailField()
    detail_desc = models.TextField()


class Skills(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()


class EducationDetails(models.Model):
    college = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    marks = models.CharField(max_length=5)
    year = models.CharField(max_length=10)
    location = models.CharField(max_length=20)
    logo = models.FilePathField(path="/img")
