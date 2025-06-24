from django.db import models
from school.models import User
from utils.choices import EDUCATION_LEVEL_CHOICES, RELATIONSHIP_DEGREE_CHOICES, SEX_CHOICES

class Parent(models.Model):
    content_type='Parent'
    name = models.CharField(max_length=300)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=SEX_CHOICES)
    contact = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=500)
    notes = models.TextField(blank=True, null=True)
    education_level = models.CharField(
        max_length=20,
        choices=EDUCATION_LEVEL_CHOICES
    )
    relationship_degree = models.CharField(
        max_length=20,
        choices=RELATIONSHIP_DEGREE_CHOICES
    )
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=20)  # Armazena hash de senha idealmente

    def __str__(self):
        return f"{self.name} ({self.get_relationship_degree_display()})"
