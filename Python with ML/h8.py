#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Functions 

def funtion1():
    print("Hello, Knowlege shelf")
    


# In[4]:


'''
1. No argu no return type.
'''
def add():
    var1 = int(input("Enter the value of num1: "))
    var2 = int(input("Enter the value of num2: "))
    var3 = var1 + var2
    print("sum = ",var3)
    


# In[6]:


'''
2. With argument and no return type
'''
def sub(var1,var2):
    var3 = var1 - var2
    print("sub = ",var3)


# In[8]:


'''
3. No argument and with return type
'''
def multiply():
    var1 = int(input("Enter the value of num1: "))
    var2 = int(input("Enter the value of num2: "))  
    var3 = var1 * var2
    return var3
    


# In[9]:


'''
3. With argument and with return type
'''
def div(var1,var2):  
    var3 = var1 / var2
    return var3

