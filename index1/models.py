from django.db import models
import uuid
# from PIL import image

# Create your models here.
my_choice=[
    ('blog','Post1'),
    ('photos','Post2'),
    ('images','Post3'),
]

class TestFieldType(models.Model):
    bool=models.BooleanField(default=True)

    char=models.CharField(verbose_name='new_name',
                        max_length=200,
                        unique=True,
                        help_text='Only For Name')

    date=models.DateField(auto_now=True)

    decimal=models.DecimalField(max_digits=5,decimal_places=2)

    email=models.EmailField(max_length=100)

    text=models.TextField()
    # text1=models.TextChoices()

class FieldTypes1(models.Model):
    bin=models.BinaryField(max_length=5)
    file=models.FileField(upload_to='uploads',blank=True)

class Cars(models.Model):
    bool=models.BooleanField(default=True)
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=10)
    image=models.ImageField(upload_to='upload_image')
    file=models.FileField(upload_to='uploads',max_length=100,blank=True)

class FieldTypes2(models.Model):
    post=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5,decimal_places=4)
    age=models.PositiveIntegerField()
    number=models.IntegerField()
    email=models.EmailField(max_length=100)
    date=models.DateTimeField(auto_now=True)
    file=models.FileField(upload_to="uploads",default=True)
    url=models.URLField(max_length=200)
    text=models.TextField()
    date_time=models.DateTimeField(auto_now_add=True)
    post_choics=models.CharField(max_length=100,null=True)

class FieldTypes3(models.Model):
    duration=models.DurationField()
    time=models.TimeField(auto_now=True)
    uuid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    small=models.FloatField(max_length=100)
    slug=models.SlugField(max_length=100,default=True,help_text='this text is name with add(_)')
    duration=models.DurationField()




    