# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:18:03 2024

@author: Administrator
"""

v_lst=[]

class vehicle_profile: #vechicle class
    def __init__(self,v_name='',v_model='',v_connectivity='',v_owner='',v_features=[]):
        self.__vehicle_name=v_name
        self.__vehicle_model=v_model
        self.__vehicle_connectivity_support=v_connectivity
        self.__vehicle_owner=v_owner
        self.__vehicle_features=v_features
       
       
    def get_vehicle_owner(self,vehicle_profile): # get method to get  vehicle owner name
        return self.__vehicle_owner
       
        
    def add_new_vehicle(): #add method to add new vehicle  list
        v_name=input("Enter vehicle name")
        v_model=input("Enter vehicle model")
        v_connectivity=input("Enter vehicle connectivity")
        v_owner=input("Enter owner")
        v_features=input("Enter features")
        sublst=v_features.split(",")
           
        #add value for first time into empty list
        d=vehicle_profile(v_name,v_model,v_connectivity,v_owner,sublst)
        v_lst.append(d)
                
        for i in v_lst:
            if v_owner!=i.get__vehicle_owner(): # to check wheather the vehicle owner exists in the list
               d=vehicle_profile(v_name,v_model,v_connectivity,v_owner,sublst)
               v_lst.append(d)
                
            else:
                print("Vehicle owner exist")
     
    def display_vehicle_details():#display all the vehicle owner deatils
        print(v_lst)
        
        
    def update_vehicle_detils():#update the vehicle features details
        v_owner=input("Enter owner")
        
        for i in v_lst:
            
            if v_owner==i.get_vehicle_owner():#check weather the vehicle owner exists
                v_features=("Enter the features to update")
                i['__vehicle_features']=v_features.split(',')
                
            else:
                print("Vehicle owner dosen't exist")
                
    def delete_vehicle_details():
         v_owner=input("Enter owner")
         
         for i in v_lst:
            
            if v_owner==i.get_vehicle_owner():#check weather the vehicle owner exist
                v_lst.remove(i)
                
            else:
                print("Vehicle owner dosen't exist")
            

choice=0

while choice!=5: #keep on displaying the menue until user enters 5 to exit
    
    choice=int(input(""" 1. Add new vehicle
                         2. Display all vehicle details
                         3. Update vehicle features
                         4. Delete vehicle owner
                         5.Exit """))
                         
    match choice:
        case 1:
            vehicle_profile.add_new_vehicle() #calling add method to add vehicles
            
        case 2:
            vehicle_profile.display_vehicle_details() #calling dispaly method to dispaly vehicles list
            
        case 3:
            vehicle_profile.update_vehicle_detils() #calling  update method to update the deatils
            
        case 4:
            vehicle_profile.delete_vehicle_details() #calling delete method to delete the deatils
            
        case 5:
            print("Thank you vist again.....")
            
        case _:
            print("Invalid input")
            
        
                
                
        
            
