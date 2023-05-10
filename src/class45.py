def create_student(name, korean, math, english, science):
    return {'name':name, 
            'korean':korean, 
            'math':math, 
            'english':english, 
            'science':science
            }
    
def get_sum(student):
    return student['korean']+student['math']+student['english']+student['science']

def get_avr(student):
    return get_sum(student)/4

def student_to_string(student):
    return f"{student['name']}\t{get_sum(student)}\t{get_avr(student)}"

def main():
    students=[
        create_student('윤인성', 67, 43, 70, 56),
        create_student('연하진', 47, 60, 56, 43),
        create_student('구자연', 88, 50, 74, 16),
    ]

    print("이름\t총점\t평균")
    for student in students:
        print(student_to_string(student))
        
if __name__ == '__main__':
    main()