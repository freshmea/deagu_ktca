def generater():
    print("함수가 호출 되었습니다.")
    yield "test"


def main():
    print("A 지점 통과")
    generater()
    print("B 지점 통과")
    generater()
    print(generater())


if __name__ == "__main__":
    main()
