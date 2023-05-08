def main():
    a = 1111.2345
    print('{:.2f}'.format(a))
    print(f'{a:.2f}')
    print(f'{a:010.2f}')
    
    a= 'choi'
    print(a.upper())
    a = 'CHOI'
    print(a.lower())
    a = '    choi    '
    print(a.strip()+'end')
    
    string = 'this is a python class in deagu.'
    print(string.find('a'))
    print(string.rfind('a'))
    print(string.find('x'))
    print('python'in string)

    list_string = string.split()
    print(list_string)
    print(list_string[3])
    for i in list_string:
        print('a' in i)
    
    
if __name__ == '__main__':
    main()