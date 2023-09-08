def main():
    file = open("data/hello.txt", "x")
    file.write("hi\n")
    file.write("there\n")
    file.write("!!\n")
    file.close()


if __name__ == "__main__":
    main()
