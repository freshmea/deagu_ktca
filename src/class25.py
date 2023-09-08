def multi_return():
    a = 10
    b = 20
    c = 30
    return a, b, c


def main():
    re_a = multi_return()
    print(list(re_a)[2])
    # print(re_b)
    # print(re_c)


if __name__ == "__main__":
    main()
