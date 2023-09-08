class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avr(self):
        return self.get_sum() / 4

    def student_to_string(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_avr()}"


def main():
    students = [
        Student("윤인성", 67, 43, 70, 56),
        Student("연하진", 47, 60, 56, 43),
        Student("구자연", 88, 50, 74, 16),
    ]

    student1 = Student("이름", 11, 11, 11, 11)
    student1.get_avr()
    print(student1.math)
    # print(students[0].name)
    # print(students[0].science)
    # print(students[0].get_sum())
    # print(students[0].get_avr())

    print("이름\t총점\t평균")
    for student in students:
        print(student.student_to_string())


if __name__ == "__main__":
    main()
