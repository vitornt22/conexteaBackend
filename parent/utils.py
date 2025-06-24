from utils.choices import ACTIVITY_TYPE_CHOICES, PARTICIPATION_CHOICES, SUBJECT_CHOICES


EMOTION_MAP = {
    1: 'joy',
    2: 'anger',
    3: 'ennui',
    4: 'embarrassment',
    5: 'disgust',
    6: 'sadness',
    7: 'anxiety',
    8: 'fear',
}

EMOTION_PORTUGUESE_MAP = {
    1: "Feliz",
    2: "Raiva",
    3: "Tristeza",
    4: "Medo",
    5: "Surpreso",
    6: "Calmo",
    7: "Ansiedade"
    # complete conforme suas emoções
}

PICTOGRAM_MAP = {
    1: {"name": "Ir ao Banheiro", "path": "bathroom"},
    2: {"name": "Comer/Lanchar", "path": "food"},
    3: {"name": "Dor/Doente", "path": "sick"},
    4: {"name": "Descansar/Dormir", "path": "rest"},
    5: {"name": "Lavar as Mãos/Banhar", "path": "washing"},
    6: {"name": "Beber Água", "path": "water"}
}

ACTIVITY_TYPE_MAP = dict(ACTIVITY_TYPE_CHOICES)
PARTICIPATION_MAP = dict(PARTICIPATION_CHOICES)
SUBJECT_MAP_PT = dict(SUBJECT_CHOICES)


