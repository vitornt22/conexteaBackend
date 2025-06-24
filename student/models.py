from django.db import models
from parent.models import Parent
from school.models import School, SchoolClass
from utils.choices import AUTISM_LEVEL_CHOICES, GRADE_LEVEL_CHOICES, SEX_CHOICES, SUPPORT_LEVEL_CHOICES

class Student(models.Model):
    ## add school info in the react native screens
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    parent= models.OneToOneField(Parent,on_delete=models.SET_NULL,null=True, related_name='student' )
    name = models.CharField(max_length=255)
    education_level = models.CharField(max_length=30,
        choices=GRADE_LEVEL_CHOICES, blank=False)
    gender = models.CharField(max_length=1, choices=SEX_CHOICES)
    autism_level = models.PositiveIntegerField(choices=AUTISM_LEVEL_CHOICES)
    preferences = models.TextField(blank=True)
    comorbidades = models.TextField(
        blank=True, default=list) 
    triggers_sensitivities = models.TextField(blank=True)
    birthdate = models.DateField( blank=False)
    school_class = models.ForeignKey(
        SchoolClass, on_delete=models.CASCADE, related_name='students')
    support_level = models.CharField(
        max_length=10, choices=SUPPORT_LEVEL_CHOICES)
    what_helps_to_calm_down= models.TextField(blank=True)

    def __str__(self):
        return self.name
