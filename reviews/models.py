# Create your models here.
from django.db import models
from student.models import Student
from teacher.models import  Teacher
from utils.choices import ACTIVITY_TYPE_CHOICES, ASSESSMENT_CHOICE, PARTICIPATION_CHOICES
from datetime import timedelta
from django.utils import timezone

from django.db import models

# Create your models here.
class CheckIn(models.Model):
	teacher = models.ForeignKey(
		Teacher,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='checkins'
	)
	student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='checkins')
	date= models.DateField(blank=True, null=True)
	emoction_id= models.IntegerField(blank=False, null=False)
	description=models.CharField(max_length=1000)

	def save(self, *args, **kwargs):
		if self.date is None:
			self.date= timezone.now().date()
		super().save(*args, **kwargs)

class ActionModel(models.Model):
	teacher = models.ForeignKey(
		Teacher,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='actions'
	)
	student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='actions')
	date= models.DateField(blank=True, null=True)
	emoction_id= models.IntegerField(blank=False, null=False)
	description=models.CharField(max_length=1000)

	def save(self, *args, **kwargs):
		if self.date is None:
			self.date= timezone.now().date()
		super().save(*args, **kwargs)

class Activity(models.Model):
	teacher = models.ForeignKey(
		Teacher,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='activities'
	)
	student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='activities')

	activity_type = models.CharField(
        max_length=1,
        choices=ACTIVITY_TYPE_CHOICES,
        blank=False
    )
	participation = models.CharField(
		max_length=1,
		choices=PARTICIPATION_CHOICES,
		blank=False
	)
	description= models.CharField( max_length=800)
	student_performance= models.CharField( max_length=800)
	date= models.DateField(blank=True, null=True)
	
    

	def save(self, *args, **kwargs):
		if self.date is None:
			self.date= timezone.now().date()
		super().save(*args, **kwargs)

class ReviewModel(models.Model):
	teacher = models.ForeignKey(
		Teacher,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='reviews'
	)
	student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='reviews')
	date= models.DateField(blank=True, null=True)
	interation= models.IntegerField(choices=ASSESSMENT_CHOICE)
	concentration= models.IntegerField(choices=ASSESSMENT_CHOICE)
	autonomy= models.IntegerField(choices=ASSESSMENT_CHOICE)
	comunication= models.IntegerField(choices=ASSESSMENT_CHOICE)
	problemSolving= models.IntegerField(choices=ASSESSMENT_CHOICE)
	compreension= models.IntegerField(choices=ASSESSMENT_CHOICE)
	regulation= models.IntegerField(choices=ASSESSMENT_CHOICE)
	respect= models.IntegerField(choices=ASSESSMENT_CHOICE)
	resistance= models.IntegerField(choices=ASSESSMENT_CHOICE)
	challenges= models.IntegerField(choices=ASSESSMENT_CHOICE)
	participation = models.IntegerField(choices=ASSESSMENT_CHOICE)
	punctuality= models.IntegerField(choices=ASSESSMENT_CHOICE)

      
	def save(self, *args, **kwargs):
		if self.date is None:
			self.date= timezone.now().date()
		super().save(*args, **kwargs)
              

class EducationPlanModel(models.Model):
		year = models.CharField(max_length=4)
		student = models.ForeignKey(
			Student, on_delete=models.CASCADE, related_name='peis'
		)
		start_date = models.DateField()
		end_date = models.DateField(blank=True, null=True)  # Troquei para DateField para ficar coerente com o nome
		objectives = models.JSONField()
		resource = models.JSONField()
		report1 = models.TextField()
		report2 = models.TextField()

		def save(self, *args, **kwargs):
			if not self.end_date and self.start_date:
				# Adiciona 365 dias ao start_date
				self.end_date = self.start_date + timedelta(days=365)
		
			super().save(*args, **kwargs)

		def __str__(self):
			return f"PEI {self.year} - {self.student.name}"




