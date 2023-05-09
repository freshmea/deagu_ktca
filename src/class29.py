def main():
    file = open('data/hello.txt', 'r')
    file.write('hi')
    file.write('there')
    file.write('!!')
    file.close()

if __name__ == '__main__':
    main()