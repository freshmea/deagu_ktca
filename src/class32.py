def main():
    with open("data/info.txt", "+r") as file:
        while contents := file.readline():
            (name, weight, height) = contents.split(", ")
            print(name, weight, height)
            bmi = int(weight) / (int(height) / 100 * int(height) / 100)
            print(name, bmi)


if __name__ == "__main__":
    main()
