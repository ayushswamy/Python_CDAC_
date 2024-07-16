# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:58:39 2024

@author: Administrator
"""
 #import re
statement=input("Enter the your statement:")
lst=[',','"','#','@','"','.']
for  i in range(len(statement)):
    if lst[i]==statement:
        statement=statement[:i]+statement[i+1:]
print(statement)

