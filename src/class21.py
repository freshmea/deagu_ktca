
def print_h(value, n):
    print(value, n)

def print_hello_n(value : str, n : int):
    for i in range(n):
        print(value)

def main():
    # print_hello_n(1234, 3)
    print_h('asdf', 'adf')
    print_h(123, 132)

if __name__ == '__main__':
    main()