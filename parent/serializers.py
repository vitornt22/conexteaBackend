from rest_framework import serializers
from student.serializers import StudentSerializer
from .models import Parent

class ParentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Parent
        fields = '__all__'  # todos os campos do Parent + o abaixo
        extra_fields = ['student']  # para clareza, mas não é obrigatório no DRF

    # Para garantir que o campo student apareça mesmo com __all__
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['student'] = StudentSerializer(instance.student).data if hasattr(instance, 'student') else None
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
