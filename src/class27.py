def power(item):
    return item * item


def under_7(item):
    return item < 7


def under_3(item):
    return item < 3


def main():
    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = map(power, list_a)
    for i in result:
        print(i)

    result = map(power, list_a)
    print(list(result))

    result = filter(under_7, list_a)
    print(list(result))
    result = filter(under_3, list_a)
    for i in result:
        if i > 3:
            break
        print(i)

    print(list(result))
    for i in result:
        print(i)


if __name__ == "__main__":
    main()
