def main():
    # 프린트 class type, auto type casting
    print(1, 2, 3, 4)
    print("1234")
    print(100 + 100)
    print("1234" + str(100 + 100))
    print(int("1234") + 100 + 100)
    print(1.1)
    print(type(1.1))
    print(5)
    print(type(5))
    print(1.1 + 5)
    print(type(1.1 + 5))

    # 식별자
    student = "최수길"
    print(student * 5)

    student_1 = "최소니"
    student_2 = "장모님"
    print(student_1, student_2)


if __name__ == "__main__":
    main()
