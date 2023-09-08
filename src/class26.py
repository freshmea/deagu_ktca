def main():
    tu = tuple((2, 3, 4))
    print(tu)
    print(tu[0])
    print(tu[0:2])
    tu_2 = tu[0:2]
    print(tu)
    print(tu_2)
    list_1 = list(tu)
    print(list_1)

    for i in tu:
        print(i)

    a = 10
    b = 20
    print(f"a : {a} ,b : {b}")

    a, b = b, a
    # temp = a
    # a = b
    # b = temp

    print(f"a : {a} ,b : {b}")


if __name__ == "__main__":
    main()
