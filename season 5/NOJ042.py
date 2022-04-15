import math


class Person:
    def __init__(self, name, weight, height, gender):
        self.name = name
        self.weight = weight
        self.height = height
        self.gender = gender

    def bmi(self):
        bmi_number = 0
        if self.gender == 'male':
            bmi_number = math.floor((self.height - 80) * 0.7)
        else:
            bmi_number = math.floor((self.height - 70) * 0.6)
        return bmi_number


s = input().split(' ')
person = Person(s[0], int(s[1]), int(s[2]), s[3])
print(person.bmi())
