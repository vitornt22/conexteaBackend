# Seu arquivo admin.py (ex: reviews/admin.py)
from django.contrib import admin
from .models import CheckIn, EducationPlanModel, ReviewModel, ActionModel, Activity, Student # Certifique-se de importar todos os seus modelos, incluindo Student

@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    # Use o método 'get_student_name' em vez de 'student.name'
    list_display = ('get_student_name', 'date')

    def get_student_name(self, obj):
        """Retorna o nome do estudante associado a este CheckIn."""
        return obj.student.name if obj.student else '-'
    get_student_name.short_description = 'Nome do Estudante' # Título da coluna no Admin

@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    # Use o método 'get_student_name' em vez de 'student.name'
    list_display = ('get_student_name', 'date')

    def get_student_name(self, obj):
        """Retorna o nome do estudante associado a esta Revisão."""
        return obj.student.name if obj.student else '-'
    get_student_name.short_description = 'Nome do Estudante'

@admin.register(ActionModel)
class ActionModelAdmin(admin.ModelAdmin):
    # Use o método 'get_student_name' em vez de 'student.name'
    list_display = ('get_student_name', 'date')

    def get_student_name(self, obj):
        """Retorna o nome do estudante associado a esta Ação."""
        return obj.student.name if obj.student else '-'
    get_student_name.short_description = 'Nome do Estudante'

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    # Use o método 'get_student_name' em vez de 'student.name'
    list_display = ('get_student_name', 'date')

    def get_student_name(self, obj):
        """Retorna o nome do estudante associado a esta Atividade."""
        return obj.student.name if obj.student else '-'
    get_student_name.short_description = 'Nome do Estudante'

@admin.register(EducationPlanModel)
class EducationPlanModelAdmin(admin.ModelAdmin):
    # Use o método 'get_student_name' em vez de 'student.name'
    list_display = ('get_student_name', 'id')

    def get_student_name(self, obj):
        """Retorna o nome do estudante associado a esta Atividade."""
        return obj.student.name if obj.student else '-'
    get_student_name.short_description = 'Nome do Estudante'