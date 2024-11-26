# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 12:30:40 2024

@author: 1mscds24
"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"hello, my name is {self.name} and I am {self.age} years old.")
class student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id
    def display_id(self):
        print(f"my student ID is {self.student_id}.")
student1=student("Bob",20,"s12345")
student1.greet()
student1.display_id()       