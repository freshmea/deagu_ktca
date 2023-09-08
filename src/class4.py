def main():
    print("안녕하세요")
    print("안녕하세요"[0])
    print("안녕하세요"[1])
    print("안녕하세요"[2])
    print("안녕하세요"[3])
    print("안녕하세요"[4])
    # 인덱스 에러 print('안녕하세요'[5])

    print(type("안녕하세요"))
    print(type("안녕하세요"[0]))

    say_hellow = "안녕하세요"
    print(say_hellow)
    print(say_hellow[0])
    print(say_hellow[1])
    print(say_hellow[2])
    print(say_hellow[3])
    print(say_hellow[4])
    # slicing [2:4)
    print(say_hellow[2:4])
    say_hellow2 = say_hellow * 3
    print(say_hellow2)
    print(say_hellow2[2:15:2])
    print(say_hellow2[-1::-1])

    for i in say_hellow:
        print(i)

    print(len(say_hellow))
    print(len(say_hellow2))

    for i in range(len(say_hellow)):
        print(say_hellow[i])

    say_hellow = 1.1
    # if type(say_hellow) == type(str()):
    if isinstance(say_hellow, str):
        print("say_hellow 변수는 str 입니다.")
    # elif type(say_hellow) == type(int()):
    if isinstance(say_hellow, int):
        print("say_hellow 변수는 int 입니다.")
    else:
        print("say_hellow 변수는 str 도 int도 아닙니다.")


if __name__ == "__main__":
    main()
