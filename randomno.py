#!/usr/bin/python3


import numpy as np


r=int(input(print("enter no. of rows :  ")))
c=int(input(print("enter no. of col :  ")))
a=np.matrix(np.random.randint(1,100, size=(r,c)))
print(a)

file=input(print("file name :  "))
f=open(file,"a+")
f.write(str(a))
f.close()

