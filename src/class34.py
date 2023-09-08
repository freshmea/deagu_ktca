def generater():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")
    yield 3


def main():
    output = generater()
    # print('D 지점 통과')
    # a = next(output)
    # print(a)

    # print('E 지점 통과')
    # b = next(output)
    # print(b)

    # c = next(output)
    # print(c)
    # print('F 지점 통과')
    for i in output:
        print("aa")
        print(i)


if __name__ == "__main__":
    main()
