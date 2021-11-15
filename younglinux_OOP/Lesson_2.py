class Person:
    def __init__(self, name, surname, qval = 1):
        self.name = name
        self.surname = surname
        self.qualification = qval

    def personal_information(self):
        print('Фамилия и имя сотрудника: ' + str(self.surname) + ' ' + str(self.name) + ' ,а его квалификация: ' + str(self.qualification))

    def __del__(self):
        print('Досвидания, мистер ' + str(self.surname) + ' ' + str(self.name))


if __name__ == '__main__':
    emp1 = Person('Ivan', 'Ivanov', 3)
    emp2 = Person('Petr', 'Petrov', 5)
    emp3 = Person('Sidr', 'Sidrov', 7)

    emp1.personal_information()
    emp2.personal_information()
    emp3.personal_information()

    emp1.__del__()
    input()