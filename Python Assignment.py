# ## Assignment Part-1
# # Q1. Why do we call Python as a general purpose and high-level programming language?

        #   Python is a popular general-purpose programming language that has a wide variety of applications.  
        #   All sorts of technological solutions have Python at their core, from web applications, search engines, 
        #   and games to animation software and even other programming languages.


# # Q2. Why is Python called a dynamically typed language?

# Python also take cares of the memory management which is crucial in programming.
# So, Python is a dynamically typed language.



# Q3. List some pros and cons of Python programming language?

# Pros of Python         |     Cons of Python
# Extensible             |      Speed Limitation           
# Number Of Libraries    | Lack of Client-Side Applications
# Easy To Understand     |  Underdeveloped Database
# IOT Ready              |
# Readable               |
# Embeddable                                 
                              


# Q4. In what all domains can we use Python?
            #   Data Science
            #  Automation 
            #  AI & Machine Learning 
            #  Application Development

# Q5. What are variable and how can we declare them?
# Variables:- Variables are nothing but reserved memory locations to store values. This means that when you create a variable you reserve some space in memory. 
#    x=2:Just define value to varible then we can use for finding type of the varible


# Q6. How can we take an input from the user in Python?
# #  By using input function we cab use input 
#  x=input("Enter the number by your choice")

# Q7. What is the default datatype of the value that has been taken as an input using input() function?
# Data type can store variable data, 
# Data type are:- Text typr,Numberic Types,srquence types,mapping type

# Q8. What is type casting?
# In Python, Type Casting is a process in which we convert a literal of one type to another.
# e.g int() ,float(),str()


# Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
a,b=input("Enter two numbers").split()
print(a,b)
output
Enter two numbers22 44
22 44


# Q10. What are keywords?
# Python keywords are special reserved words that have specific meanings and purposes and can’t be used for anything 
# but those specific purposes.

# Q11. Can we use keywords as a variable? Support your answer with reason.
    # Keywords are specific for certain opeartion we can not use keywords as variable

# Q12. What is indentation? What's the use of indentaion in Python?
# The indentation in Python is very important.
# Python uses indentation to indicate a block of code.

# Q13. How can we throw some output in Python?
# By using print function we can use to see output e .g print("Heloo World")

# Q14. What are operators in Python?

#  Python operators allow us to do common processing on variables. 
# We will look into different types of operators with examples and also operator precedence. 
# They are the special symbols that can manipulate the values of one or more operands.


# Q15. What is difference between / and // operators?
## Float Division("/"): Divides left hand operand by right hand operand.
# Floor Division("//"): The division of operands where the result is the quotient in which the digits after the decimal point are removed

# Q16. Write a code that gives following as an output.
# iNeuroniNeuroniNeuroniNeuron
---------------------
for i in range (4):
    print("iNeuron",end="")
----------------------


# Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
number=int(input("Enter the number to check even or odd ")) 
if(number %2==0):
    print(f"Number is even",number)
else:
    print(f"Number is odd",number)


# Q18. What are boolean operator?

## The logical operators and, or and not are also referred to as boolean operators. 
# While and as well as or operator needs two operands, 'AND''OR''NOT'
# which may evaluate to true or false, not operator needs one operand evaluating to true or false

# Q19. What will the output of the following?
# ```
# 1 or 0= 1

# 0 and 0= 0

# True and False and True=  False

# 1 or 0 or 0=   1
# ```


# # Q20. What are conditional statements in Python?

# This statements is use for checking  boolean operator and or not
#     using if-else ,if-elif condition for True or False: 


# Q21. What is use of 'if', 'elif' and 'else' keywords?
# #For checking condition for if true or false .elif  condition is true  check other if that is true or not .
# An else statement can be combined with an if statement.
# An else statement contains the block of code that executes 
# if the conditional expression in the if statement resolves to 0 or a FALSE value.


# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

person=int(input("Enter Your age: "))
if person>=18:
    print("I can vote")
elif person<18:
    print("I can't vote")





# Q23. Write a code that displays the sum of all the even numbers from the given list.
# ```
numbers = [12, 75, 150, 180, 145, 525, 50]
sum=0
for  i in numbers:
    if i%2==0:
      sum+=i
print(sum)
           

# Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
x,y,z=input("Enter three number:-" ).split()
if x>y and  x>z:
   print("the largest number is:- ",x)
elif y>x and  y>z:
   print("the largest number is:- ",y)
else:
   print("the largest number is:- ",z)   

# Q25. Write a program to display only those numbers from a list that satisfy the following conditions


# - The number must be divisible by five

# - If the number is greater than 150, then skip it and move to the next number

# - If the number is greater than 500, then stop the loop
# ```
numbers = [12, 75, 150, 180, 145, 525, 50]
list=[]
for i in numbers:
    if (i>150):
        if  (i>500):
            break
    elif i%5==0:
        list.append(i)
print(list)
        

   
