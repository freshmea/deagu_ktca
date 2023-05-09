def print_var_value(*values):
    print(type(values))
    for i in values:
        print(i)

def main():
    print_var_value('asdf', 'choi', 'su', 'gil')

if __name__ == '__main__':
    main()