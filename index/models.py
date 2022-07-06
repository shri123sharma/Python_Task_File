from django.db import models
from datetime import datetime

# Create your models here.
class Base(models.Model):
    name=models.CharField(max_length=100,null=True)

class Child(models.Model):
    name_1=models.CharField(max_length=100)

class Student(models.Model):
    freshman='fr'
    sophomore='so'
    junior='jr'
    senior='sr'
    graduate='gr'

    year_of_in_school=[
        (freshman,'Freshman'),
        (sophomore,'Sophomore'),
        (junior,'Junior'),
        (senior,'Senior'),
        (graduate,'Graduate'),
    ]

    year_in_school=models.CharField(
        max_length=10,
        choices= year_of_in_school,
        default='Freshman',
        )

class Student1(models.Model):

    class YearInSchool(models.TextChoices):
        freshman='fr',('Freshman'),
        sophomore='so',('Sophomore'),
        junior='ju',('Junior'),
        senior='se',('Senior'),
        graduate='gu',('Graduate'),

    year_in_school=models.CharField(
        max_length=10,
        choices=YearInSchool.choices,
        default=YearInSchool.freshman,
    )

class FieldOption(models.Model):
    name=models.CharField(max_length=100,db_column='name1')
    age=models.IntegerField()
    email=models.EmailField(max_length=100,default='you101@gmail.com')

class FieldOption1(models.Model):
    number=models.IntegerField(db_index=True)

class Field(models.Model):
    number1=models.IntegerField(primary_key=True, db_index=True)
    name=models.CharField(max_length=100,db_column='name1')

class Fieldoption2(models.Model):
    name2=models.CharField(max_length=100,editable=False)
    age=models.IntegerField(default='1',db_column='age2',db_index=False)

class FieldOption3(models.Model):
    message4=models.CharField(max_length=100,help_text="this field case sensitive")

class FieldOption4(models.Model):
    user_1=models.CharField(max_length=100,primary_key=True)
    number_2=models.IntegerField(primary_key=False)

class Field1(models.Model):
    user2=models.CharField(max_length=100)
    date_of_birth=models.DateField(unique=True)
    number=models.IntegerField(unique=True)

class Field2(models.Model):
    user3=models.CharField(max_length=100,default='name',help_text='only for name',)
    title=models.CharField(max_length=100)
    number=models.IntegerField()
    user_name=models.CharField(max_length=100,unique=True,db_index=True)

class Field3(models.Model):
    id=models.AutoField(primary_key=True)
    user4=models.CharField(max_length=50)
    age4=models.IntegerField()

