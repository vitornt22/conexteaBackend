from django.db import models
from django.core.validators import RegexValidator
# vnt12345
from utils.choices import SEX_CHOICES
from django.contrib.auth.models import AbstractUser
from django.db import models

class School(models.Model):
    name = models.CharField(max_length=300)
    director_name = models.CharField(max_length=200)  # nome do diretor
    director_gender= models.CharField(max_length=1, choices=SEX_CHOICES)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=20)  # **não recomendado salvar assim**
    address = models.CharField(max_length=500)
    contact = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    inep_number = models.CharField(
        max_length=8,
        validators=[
            RegexValidator(
                regex=r'^\d{8}$',
                message='INEP number must be exactly 8 digits.'
            )
        ],
        unique=True
    )

    def __str__(self):
        return self.name

class SchoolClass(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classes')
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} - {self.year}'

class User(AbstractUser):
    USER_TYPES = (
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    def __str__(self):
        return f"{self.username} ({self.user_type})"
