def multi_return():
    a = 10
    b = 20
    c = 30
    return a, b

def main():
    re_a, re_b = multi_return()
    print(re_a)
    print(re_b)

if __name__ == '__main__':
    main()