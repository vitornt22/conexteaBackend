# utils.py

SEX_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

AUTISM_LEVEL_CHOICES = [
    (1, 'Nível 1 - Requer suporte'),
    (2, 'Nível 2 - Requer suporte substancial'),
    (3, 'Nível 3 - Requer suporte muito substancial'),
]


RELATIONSHIP_DEGREE_CHOICES = [
    ('father', 'Pai'),
    ('mother', 'Mãe'),
    ('guardian', 'Responsável Legal'),
    ('grandparent', 'Avô/Avó'),
    ('uncle_aunt', 'Tio/Tia'),
    ('sibling', 'Irmão/Irmã'),
    ('other', 'Outro'),
]

WORK_SHIFT_CHOICES = [
    ('morning', 'Manhã'),
    ('afternoon', 'Tarde'),
    ('night', 'Noite'),
]
SUPPORT_LEVEL_CHOICES = [
    ('low', 'Baixo'),
    ('medium', 'Médio'),
    ('moderate', 'Moderado'),
    ('high', 'Alto'),
]

EDUCATION_LEVEL_CHOICES = [
    ('never_studied', 'Nunca estudou'),
    ('elementary', 'Ensino Fundamental'),
    ('middle_school', 'Ensino Fundamental II'),
    ('high_school', 'Ensino Médio'),
    ('bachelor', 'Graduação'),
    ('master', 'Mestrado'),
    ('doctorate', 'Doutorado'),
]


GRADE_LEVEL_CHOICES = [
    ('preschool', 'Educação Infantil'),
    ('elementary_1', 'Ensino Fundamental I'),
    ('elementary_2', 'Ensino Fundamental II'),
    ('high_school', 'Ensino Médio'),
]


ACTIVITY_TYPE_CHOICES = [
    ('1', 'Linguagem e Comunicação'),
    ('2', 'Raciocínio e Cognitivo'),
    ('3', 'Motricidade e Coordenação'),
    ('4', 'Atividades Sensorial-Exploratórias'),
    ('5', 'Autonomia e Organização'),
    ('6', 'Interação e Participação'),
]

PARTICIPATION_CHOICES = [
    ('1', 'Não participou'),
    ('2', 'Parcialmente'),
    ('3', 'Participou'),
]

ASSESSMENT_CHOICE = [
    ('1', 'Não demonstrou'),
    ('2', 'Parcialmente'),
    ('3', 'Demonstrou plenamente'),
]


SUBJECT_CHOICES = [
    ('math', 'Matemática'),
    ('portuguese', 'Português'),
    ('science', 'Ciências'),
    ('history', 'História'),
    ('geography', 'Geografia'),
    ('physics', 'Física'),
    ('chemistry', 'Química'),
    ('biology', 'Biologia'),
    ('literature', 'Literatura'),
    ('philosophy', 'Filosofia'),
    ('sociology', 'Sociologia'),
    ('english', 'Inglês'),
    ('arts', 'Artes'),
    ('music', 'Música'),
    ('physical_ed', 'Educação Física'),
    ('psychomotor', 'Psicomotricidade'),
    ('play', 'Atividades lúdicas'),
    ('technology', 'Tecnologia'),
]
