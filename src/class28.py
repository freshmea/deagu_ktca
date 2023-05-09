def main():
    list_a = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
    
    result = map(lambda x : x * x, list_a)
    for i in result:
        print(i)
        
    result = map(lambda x : x * x, list_a)
    print(list(result))
    
    result = filter(lambda x : x < 3, list_a)
    print(list(result))
    result = filter(lambda x : x < 3, list_a)
    for i in result:
        if (i > 3):
            break
        print(i)
    
    print(list(result))
    for i in result:
        print(i)


if __name__ == '__main__':
    main()