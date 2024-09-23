import random

students=[
    'CONNOR',
    'DABUEL',
    'TREVOR',
    'PEYTON',
    'TYLER',
    'JENNA',
    'KANYON',
    'SILAS',
    'JOE',
    'PABLO',
    'TYSON',
    'DYLAN',
    'LAYLA',
    'LANDON B',
    '',
    '',
    '',
    ''
]

animals=[
'bear',
'wolf',
'cow',
'horse',
'rabbit',
'bull',
'owl',
'ape',
'parrot',
'deer',
'tigere',
'tyrtle',
'crocodile',
'elephant',
'hippo',
'giraffe',
'walrus',
'eagle',
]

for i in range (18):
    student=random.choice(students)
    animal= random.choice(animals)
    animals.remove(animal)
    students.remove(student)
    