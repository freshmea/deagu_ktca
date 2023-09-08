list_of_list = [[1, 2, 3], [4, 5, 6, 7], [8, 9], 10]


def main():
    for i in list_of_list:
        # if type(i) == type(list()):
        if isinstance(i, list):
            for j in i:
                print(j)
        else:
            print(i)


if __name__ == "__main__":
    main()
