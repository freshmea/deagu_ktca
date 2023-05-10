from class51 import Student

class CompStudent(Student):
    def __init__(self, name, korean, math, english, science):
        Student.__init__(self, name, korean, math, english, science)
        
    def __eq__(self, value):
        return self.get_avr() == value
    def __ne__(self, value):
        return self.get_avr() != value
    def __gt__(self, value):
        return self.get_avr() > value
    def __ge__(self, value):
        return self.get_avr() >= value
    def __lt__(self, value):
        return self.get_avr() < value
    def __le__(self, value):
        return self.get_avr() <= value
        
def main():
    # with open('data/students.txt', 'w') as file:
    #     file.write('wer, 34, 53, 03, 73\n')
    #     file.write('asd, 12, 23, 12, 23\n' )
    #     file.write('sdw, 100, 100, 100, 100\n' )
    #     file.write('xcv, 90, 90, 90, 90\n' )
        
    with open('data/students.txt', 'r') as file:
        while(data := file.readline()):
            (name, korean, math, english, science) = data.split(', ')
            CompStudent(name, int(korean), int(math), int(english), int(science))

    CompStudent.st_print()
    
    for person in CompStudent.students:
        print (person.name, '90점과 같은지 비교',person == 90)
        print (person.name, '90점과 같지 않은지 비교',person != 90)
        print (person.name, '90점보다 큰지 비교',person > 90)
        print (person.name, '90점과 크거나 같은지 비교',person >= 90)
        print (person.name, '90점과 작은지 비교',person < 90)
        print (person.name, '90점보다 작거나 같은지 비교',person <= 90)
    
if __name__ == '__main__':
    main()