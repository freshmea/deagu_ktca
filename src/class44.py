students = [
    {"name": "윤인성", "korean": 67, "math": 43, "english": 70, "science": 56},
    {"name": "연하진", "korean": 47, "math": 60, "english": 56, "science": 43},
    {"name": "구자연", "korean": 88, "math": 50, "english": 74, "science": 16},
]

print("이름, 총점, 평균")
for student in students:
    sum = student["korean"] + student["math"] + student["english"] + student["science"]
    print(student["name"], sum, sum / 4)
