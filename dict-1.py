# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:27:33 2024

@author: 1mscds24
"""

name=[]
salary=[]
emp_name={'em_nm':name,'salary':salary}
choice=1
while choice!=0:
    print("1.add empl detail")
    print("2.show all employ details")
    print("3.search employ")
    print("0.quit")
choice=int(input("enter ur choice:"))
if choice==1:
    name=input("enter ur name:")
    salary=int(input("enter salary"))
    name.append(name)
    salary.append(salary)
elif choice==2:
    print("*** emp details***")
    print("%20s"%"NAME","%10s"%"salary")
    print("-------")
    n=emp_name['em_nm']
    s=emp_name['salary']
    for i in range (len(n)):
        print("%20s")
        