# class Student:
#   marks = 0

#   def compute_marks(self, obtained_marks):
#     marks = obtained_marks
#     print('Obtained Marks:', marks)

# # convert compute_marks() to class method
# Student.print_marks = classmethod(Student.compute_marks)
# Student.print_marks(88)

# Output: Obtained Marks: 88
# from datetime import date

# # random Person
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def fromBirthYear(cls, name, birthYear):
#         return cls(name, date.today().year - birthYear)

#     def display(self):
#         print(self.name + "'s age is: " + str(self.age))

# person = Person('Adam', 19)
# person.display()

# person1 = Person.fromBirthYear('John',  1985)
# # person1.display()


from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Male'

man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))