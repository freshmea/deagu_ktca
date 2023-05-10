def print_default(value : str, n: int = 5):
    for i in range(n):
        print(value)

def main():
    print_default('hi', 2)
    # print_default('hi', 2)

if __name__ == '__main__':
    main()