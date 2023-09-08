def main():
    color_list = ["red", "yellow", "white", "blue", "orange", "green", "navy", "purple"]
    for i, value in enumerate(color_list):
        print(i, "번째 변수는 :", value)

    dict_a = {"choi": 170, "kim": 165, "lee": 180, "su": 150, "park": 177}

    for key, value in dict_a.items():
        print(key, "키의 값은 : ", value)


if __name__ == "__main__":
    main()
