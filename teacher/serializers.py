from rest_framework import serializers

from utils.choices import SUBJECT_CHOICES
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
