def multiple( a = 2, b= 2, n = 1):
    result = a
    for i in range(n):
        result *= b
        
    return result

def main():
    print(multiple(n = 3, b =3))

if __name__ == '__main__':
    main()