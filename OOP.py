# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 12:16:55 2024

@author: 1mscds24
"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"hello, my name is {self.name} and I am {self.age} years old.")
Person1=Person("alice",30)
Person1.greet()
        