class Student:
    count = int()
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        print(f'{Student.count} 번째 학생이 만들어 졌습니다.')

    def get_sum(self):
        return self.korean+self.math+self.english+self.science

    def get_avr(self):
        return self.get_sum()/4
    
    def __str__(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_avr()}"
    
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    
def main():
    students=[
        Student('윤인성', 67, 43, 70, 56),
        Student('연하진', 47, 60, 56, 43),
        Student('구자연', 88, 50, 74, 16),
        Student('아무개', 80, 80, 60, 16)
    ]
    
    # student1 = Student('이름', 11, 11, 11, 11)
    # student1.get_avr()
    # print(student1.math)
    # print(students[0].name)
    # print(students[0].science)
    # print(students[0].get_sum())
    # print(students[0].get_avr())

    # print("이름\t총점\t평균")
    # for student in students:
    #     print(student.student_to_string())
        
    print("이름\t총점\t평균")
    for student in students:
        print(student)
    
    print(students[0] == students[3])
    print(students[0] != students[3])
    print(students[0] != students[1])
    print(Student.count)
if __name__ == '__main__':
    main()