from urllib import request


def main():
    print("프로그램 시작합니다.")
    target = request.urlopen("https://google.com")

    output = target.read()
    print(output)

    print("프로그램 끝났습니다.")


if __name__ == "__main__":
    main()
