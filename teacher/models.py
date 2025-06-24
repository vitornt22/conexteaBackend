from django.db import models

# Create your models here.
from django.db import models
from school.models import School, SchoolClass, User
from utils.choices import  GRADE_LEVEL_CHOICES, SEX_CHOICES, SUBJECT_CHOICES, WORK_SHIFT_CHOICES


class Teacher(models.Model):
    ## add school info in the react native screens
    content_type='Teacher'
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')
    name = models.CharField(max_length=300, blank=False)
    registration_id = models.CharField(max_length=100, blank=True)
    work_start= models.DateField()
    sexo = models.CharField(max_length=1, choices=SEX_CHOICES)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=20)  
    nickName = models.CharField(max_length=300, blank=True, null=True)
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES, blank=False, null=False)
    work_shift = models.CharField(max_length=100, choices=WORK_SHIFT_CHOICES)
    has_specialization = models.BooleanField(default=False)
    education_level = models.CharField(max_length=100,
        choices=GRADE_LEVEL_CHOICES, blank=False)
    birthdate = models.DateField( blank=False)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.SET_NULL, null=True, related_name='teachers')


    def __str__(self):
        return self.name



