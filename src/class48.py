class Student:
    def __init__(self) -> None:
        pass

    def study(self):
        print("공부를 합니다.")


class Teacher:
    def __init__(self) -> None:
        pass

    def teach(self):
        print("강의를 합니다.")


def main():
    person = [Student(), Student(), Student(), Teacher(), Student()]
    for per in person:
        if isinstance(per, Student):
            per.study()
        elif isinstance(per, Teacher):
            per.teach()


if __name__ == "__main__":
    main()
