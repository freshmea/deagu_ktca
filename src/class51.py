class Student:
    count = int()
    students = list()
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)
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
    
    @classmethod
    def st_print(cls):
        print('------ 학생목록 ------')
        print(f'------ 총학생수 : {cls.count}')
        print('이름\t총점\t평균')
        for student in cls.students:
            print(student)
        print('-----------------------')
    
def main():
    Student('윤인성', 67, 43, 70, 56)
    Student('연하진', 47, 60, 56, 43)
    Student('구자연', 88, 50, 74, 16)
    Student('아무개', 80, 80, 60, 16)
    
    Student.st_print()

if __name__ == '__main__':
    main()