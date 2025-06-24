from django.http import JsonResponse
from student.models import Student

def gerar_alunos(request):
        try:
            teacher = Teacher.objects.get(id=2)
        except Teacher.DoesNotExist:
            return Response({'detail': 'Teacher not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        if teacher.school_class_id is None:
            # professor não tem turma vinculada, retorna lista vazia
            students = Student.objects.none()
        else:
            students = Student.objects.filter(school_class_id=teacher.school_class_id)

        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

from django.http import HttpResponse
from datetime import date, timedelta
from student.models import Student
from teacher.models import Teacher
from reviews.models import CheckIn, ActionModel, Activity, ReviewModel
import random

def populate_student_records(request):
    start_date = date(date.today().year, 2, 1)
    end_date = date.today() - timedelta(days=1)
    students = Student.objects.filter(id__gte=11, id__lte=20)
    teacher = Teacher.objects.get(id=2)

    descriptions_checkin = [
        "Chegou tranquilo e atento às orientações.",
        "Mostrou-se um pouco ansioso ao chegar.",
        "Chegou animado e interativo com os colegas.",
        "Estava calmo, porém reservado ao chegar."
    ]

    descriptions_action = [
        "Teve iniciativa ao ajudar um colega.",
        "Realizou a atividade com apoio do professor.",
        "Mostrou interesse durante a tarefa.",
        "Apresentou certa resistência, mas concluiu com suporte."
    ]

    activity_comments = {
        '1': "Participou das atividades de leitura e comunicação, interagindo com os colegas.",
        '2': "Demonstrou bom raciocínio em desafios cognitivos e jogos de lógica.",
        '3': "Praticou movimentos e atividades motoras com dedicação.",
        '4': "Explorou os materiais sensoriais com curiosidade e atenção.",
        '5': "Organizou seus materiais de forma autônoma e ordenada.",
        '6': "Interagiu positivamente com os colegas durante as dinâmicas."
    }

    participation_choices = ['1', '2', '3']
    activity_types = ['1', '2', '3', '4', '5', '6']
    assessment_choices = ['1', '2', '3']

    current_date = start_date
    while current_date <= end_date:
        for student in students:
            # CheckIn
            CheckIn.objects.create(
                teacher=teacher,
                student=student,
                date=current_date,
                emoction_id=random.randint(1, 5),
                description=random.choice(descriptions_checkin)
            )

            # ActionModel
            ActionModel.objects.create(
                teacher=teacher,
                student=student,
                date=current_date,
                emoction_id=random.randint(1, 5),
                description=random.choice(descriptions_action)
            )

            # Activity
            activity_type = random.choice(activity_types)
            participation = random.choice(participation_choices)
            Activity.objects.create(
                teacher=teacher,
                student=student,
                date=current_date,
                activity_type=activity_type,
                participation=participation,
                description=activity_comments[activity_type],
                student_performance="Desempenho adequado ao esperado para a atividade proposta."
            )

            # ReviewModel
            ReviewModel.objects.create(
                teacher=teacher,
                student=student,
                date=current_date,
                interation=random.choice(assessment_choices),
                concentration=random.choice(assessment_choices),
                autonomy=random.choice(assessment_choices),
                comunication=random.choice(assessment_choices),
                problemSolving=random.choice(assessment_choices),
                compreension=random.choice(assessment_choices),
                regulation=random.choice(assessment_choices),
                respect=random.choice(assessment_choices),
                resistance=random.choice(assessment_choices),
                challenges=random.choice(assessment_choices),
                participation=random.choice(assessment_choices),
                punctuality=random.choice(assessment_choices)
            )

        current_date += timedelta(days=1)

    return HttpResponse("Registros criados com sucesso!")
