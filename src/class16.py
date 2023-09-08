def main():
    character = {
        "name": "기사",
        "level": 12,
        "items": {"sword": "불꽃의 검", "amor": "풀플레이트"},
        "skill": ["베기", "세게 베기", "아주 세게 베기"],
    }
    for i in character:
        # if type(character[i]) == type(dict()) or type(character[i]) == type(list()):
        if isinstance(character[i], dict) or isinstance(character[i], list):
            for j in character[i]:
                print(i + " : ", j)
        else:
            print(i + " : ", character[i])


if __name__ == "__main__":
    main()
