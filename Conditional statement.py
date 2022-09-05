#!/usr/bin/env python
# coding: utf-8

# #### 1.w.a.p to check whether number is even or odd

# In[1]:



x=int(input('enter the number'))
if x%2==0:
    print('even')
else:
    print('odd')


# #### 2.w.a.p check whether an Aplhabet is vowel or Consonant.

# In[2]:



x=input('enter the alphabet ')
y=['a','e','i','o','u']
if x in y:
    print('it is a vowel ')
else:
    print('it is consonant')
    


# #### 3.w.a.p to check whether person is eligible to vote or not.

# In[3]:


x=int(input('enter the age '))
if x >= 18:
    print('Eligible to vote ')
else:
    print('Not Eligble to vote!!!!')


# ####  4.w.a.p to check whether a number is positive or negetive

# In[4]:


x=int(input('enter the number '))
if x > 0:
    print('Positive ')
elif x < 0:
    print('Negative ')
elif x == 0:
    print('zero')


# ### 5.w.a.p to check whether given year is leap year or not.

# In[5]:


year=int(input('enter the leap year'))
if (year % 4 ==0) and (year % 100 != 0):
    print(" is a leap year")
elif (year % 400 == 0) and (year % 100 == 0):
    print(" is a leap year")
else:
    print("not a leap year")
    


# ### 6.w.a.p to check whether triangle is equilateral,Isosceles, or Scalene.

# In[6]:



a=int(input('enter first angle '))
b=int(input('enter second angle '))
c=int(input('enter third angle'))

if a==b and b==c and c==a:
    print("Equilateral")
elif a==b or b==c or a==c:
    print("isosecelles")
else :
    print("scalene")


# ### 7.w.a.p to check whether after selling a product it's profit or loss.

# In[7]:


sp=int(input('enter the selling price '))
cp=int(input('enter the cost price '))
p=sp-cp
if sp > cp:
    print('profit')
elif sp < cp:
    print('loss')
else:
    print('No profit')
print(p)


# ### 9.w.a.p to enter two numbers and print greatest number.

# In[8]:


x=int(input('Enter 1 number'))
y=int(input('Enter 2 number'))
if x<y:
    print('Greatest number is',y)
elif y<x:
    print('Greatest number is',x)
else:
    print('not valid')


# ### 9. Enter two numbers and enter smallest number.

# In[9]:


x=int(input('Enter 1 number'))
y=int(input('Enter 2 number'))
if x<y:
    print('smallest number is',x)
elif y<x:
    print('smallest number is',y)
else:
    print('not valid')


# ### Enter Three numbers and print greatest number.

# In[10]:


x=int(input('Enter 1 number'))
y=int(input('Enter 2 number'))
z=int(input('Enter 3 number'))
if y<x and z<x:
    print('Greatest number is',x)

elif x<y and z<y:
    print('Greatest number is',y)

elif x<z and y<z:
    print('Greatest number is',z)
    
else:
    print('Not valid')


# ### 10.Calculate Roots of Quadratic Equation.

# In[11]:


a=int(input('enter the a '))
b=int(input('enter the b '))
c=int(input('enter the c '))
z=(b**2)-(4*a*c)/(2*a)
print(z)


# ### 11.Enter a number between(1-7) and print respective day of week.

# In[12]:


a=int(input('enter number between 1-7 for the name of day '))
if a==1:
    print('Sunday')
elif a==2:
    print('Monday')    
elif a==3:
    print('Tuesday')    
elif a==4:
    print('Wednesday')    
elif a==5:
    print('Thursday')    
elif a==6:
    print('Friday')    
elif a==7:
    print('Saturday')    
else:
    print('Not valid')


# ### 12.Enter a number between(1-12) and print respective month 

# In[13]:


a=int(input('enter number between 1-12 for the month : '))
if a==1:
    print('jan')
elif a==2:
    print('Feb')    
elif a==3:
    print('Mar')    
elif a==4:
    print('Apr')    
elif a==5:
    print('May')    
elif a==6:
    print('Jun')    
elif a==7:
    print('Jul')    
elif a==8:
    print('Aug')    
elif a==9:
    print('Sep')    
elif a==10:
    print('Oct')    
elif a==11:
    print('Nov')    
elif a==12:
    print('Dec')    
else:
    print('enter valid number between 1-12')
    


# ### 13.Enter a number between(1-4) and perform following Operations:
#     -Addition
#     -Subtraction
#     -Multiplication
#     -Division

# In[14]:


a=int(input('enter the first number'))
b=int(input('enter the second number'))
num=int(input('''enter the operation number to operate
1- Addition
2- Subtration
3- Multiplication
4- Division'''))
if num==1:
    r=a+b
    print('Addition of',a,'and',b,'is',r)
elif num==2:
    r=a-b
    print('Subtration of',a,'and',b,'is',r)
elif num==3:
    r=a*b
    print('Multiplication of',a,'and',b,'is',r)
elif num==4:
    r=a/b
    print('Divison of',a,'and',b,'is',r)
else:
    print('enter number 1-4 for operation')


# ### 14.Convert to and from Celsius, Fahrenheit.

# In[15]:


a=int(input('enter 1 for Celsius to Fahrenheit conversion: \n2 for Fahrenheit to Celsius conversion '))
if a==1:
    x=int(input('Enter the temperature in Celsius'))
    y=(x*1.8)+32
    print('The temerature in Fahrenheit is',y)
    
if a==2:
    x=int(input('Enter the temperature in Fahrenheit'))
    y=((x-32)*5)/9
    print('The temerature in Celcius is',y)


# ### 15.Check if a employee is working more than 5 years and if yes add 5% Bonus

# In[16]:


salary =  int(input("enter your salary:"))
service_yrs = int(input("enter years of service:"))
if service_yrs > 5:
    print("yours salary(+bonus) = ",salary + (salary)*0.05)
else:
    print("You are not eligible for bonus as you have less service years.")


# ### 16.Check by length and breadth whether  its Square or not

# In[17]:


l= int(input("Enter the Length"))
b=int(input("Enter the Breadth"))

if   l==b:
    print("its a square")
else:
    print("its an rectangle")


# ### 17.Enter 3 people ages and print youngest and oldest.

# In[18]:


age1=int(input('enter age1: '))
age2=int(input('enter age2: '))
age3=int(input('enter age3: '))


if age1>age2 and age1>age3:
    print(age1," is oldest")
elif age2>age1 and age2>age3:
    print(age2," is oldest")
elif age3>age1 and age3>age2:
    print(age3," is oldest")
else:
    print(" NOT VALID")
    
    
if age1<age2 and age1<age3:
    print(age1," is youngest")
elif age2<age1 and age2<age3:
    print(age2," is youngest")
elif age3<age1 and age3<age2:
    print(age3," is youngest")
else:
     print("NOT VALID")


# ### School has grading system print grade as follows:-
#     - > 80 (A grade)
#     -60 to 80 (B grade)
#     -50 to 60 (C grade)
#     -45 to 50 (D grade)
#     -25 to 45 (E grade)
#     -< 25 (F grade)
#     

# In[19]:


marks=int(input("enter the  marks"))
if marks < 25:
    print("GRADE F")
elif 25 <= marks <=45:
    print("GRADE E")
elif 45 <= marks <=50:
    print("GRADE D")
elif 50 <= marks <=60:
    print("GRADE C")
elif 60 <= marks <=80:
    print("GRADE B")
elif  marks > 80:
    print(" GRADE A")
else :
    print("NOT VAID")


# In[ ]:




