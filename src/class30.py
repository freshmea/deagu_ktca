def main():
    # with open('data/hello.txt', 'r') as file:
    #     contents = str()
    #     contents = file.readline()
    #     while(contents):
    #         print(contents)
    #         contents = file.readline()

    with open("data/hello.txt", "+r") as file:
        while contents := file.readline():
            print(contents)


if __name__ == "__main__":
    main()
