import datetime


def main():
    ptime = datetime.datetime.now()
    print(ptime)
    print(int(str(ptime)[5:7]))

    print(ptime.month)
    print(type(ptime.month))

    if ptime.hour < 12:
        print("지금은 오전입니다.")
    else:
        print("지금은 오후입니다.")


if __name__ == "__main__":
    main()
