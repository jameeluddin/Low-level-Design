from abc import ABC, abstractmethod

from Design_patterns.BuilderDesignPattern.student import Student


class StudentBuilder(ABC):
    def __init__(self):
        self.roll_number = None
        self.age = None
        self.name = None
        self.father_name = None
        self.mother_name = None
        self.subjects = None

    def set_roll_number(self, roll_number):
        self.roll_number = roll_number
        return self

    def set_age(self, age):
        self.age = age
        return self

    def set_name(self, name):
        self.name = name
        return self

    def set_father_name(self, father_name):
        self.father_name = father_name
        return self

    def set_mother_name(self, mother_name):
        self.mother_name = mother_name
        return self

    @abstractmethod
    def set_subjects(self):
        pass

    def build(self):
        return Student(self)

