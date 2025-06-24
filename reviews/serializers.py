from rest_framework import serializers
from .models import (
    CheckIn,
    ActionModel,
    Activity,
    ReviewModel,
    EducationPlanModel
)

class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = '__all__'

class ActionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionModel
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'

class EducationPlanModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationPlanModel
        fields = '__all__'
