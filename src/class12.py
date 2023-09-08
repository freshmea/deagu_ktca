import random


def main():
    var = random.randint(1, 30000)
    print(f"변수는 : {var}")
    # if (var == 2 or var == 4 or var == 6 or var == 8 or var == 10):

    # 2 의 배수이면서 3의 배수가 아닌 수
    if var % 2 == 0 and not (var % 3 == 0):
        print("이 숫자는 2 의 배수이면서 3의 배수가 아닌 수다.")
    else:
        print("이 숫자는 2 의 배수이면서 3의 배수가 아닌 수가 아니다.")

    # if var % 7 == 0:
    #     print('이 숫자는 7의 배수이다.')
    # else:
    #     if var % 13 == 0:
    #         print('이 숫자는 13의 배수이다.')
    #     else:
    #         print('이 숫자는 7의 배수가 아니면서 13의 배수가 아니다.')

    if var % 7 == 0:
        print("이 숫자는 7의 배수이다.")
    elif var % 13 == 0:
        print("이 숫자는 13의 배수이다.")
    else:
        print("이 숫자는 7의 배수가 아니면서 13의 배수가 아니다.")

    x = 15
    if 10 < x < 20:
        print("x 는 10보다 크고 20보다 작다.")


if __name__ == "__main__":
    main()
