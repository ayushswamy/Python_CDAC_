# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:02:31 2024

@author: Administrator
"""
import pandas as pd #importing pands

# lst1 stores id name and company name
lst1=[['id','name','company'],['6001','amit','cdac'],['6002','mohit','cdac'],['6003','vijay','cdac'],
      ['6004','snehal','cdac'],['6005','sneha','çdac']]

#lst 2 stores id and salary
lst2=[['id','salary'],['6001',50000],['6002',60000],['6003',63000],['6004',47000],['6005',89999]]

#df1 is lst1 coverted to data frame
df1=pd.DataFrame(lst1)
df1


#df2 is lst2 coverted to data frame
df2=pd.DataFrame(lst2)
df2

#df is coverted to  final data frame my merginging two frames
df=pd.merge(df1,df2,how="inner",on=0)
df