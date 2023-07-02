# Q26. What is a string? How can we declare string in Python?
#Ans
# #Python string is the collection of the characters surrounded by single quotes, double quotes, or triple quotes.
# e.g str="Hi Python!"

# Q27. How can we access the string using its index?
# ans
# The index() method finds the first occurrence of the specified value.\
# string.index(value, start, end)
# txt = "Hello, welcome to my world."
# x=txt.index("t")
# print(x)

# Q28. Write a code to get the desired output of the followingP
# ```

      #string = "Big Data iNeuron"
      #print(string[9:])
# desired_output = "iNeuron"


# Q29. Write a code to get the desired output of the following
# # ans`
#          string = "Big Data iNeuron"
#          print(string[16:7:-1])
# desired_output = "norueNi"
# ```

# Q30. Resverse the string given in the above question.
#   ans    string = "Big Data iNeuron"
#           print(string[::-1])

# Q31. How can you delete entire string at once?
#ans          string = "Big Data iNeuron"
#          del string


# Q32. What is escape sequence?

# ```To insert characters that are illegal in a string, use an escape character.
#    An escape character is a backslash \ followed by the character you want to insert.````

# Q33. How can you print the below string?
# ```
# 'iNeuron's Big Data Course'
# string=" \"iNeuron's\" Big Data Course"
# print(string)

# Q34. What is a list in Python?
# Lists are used to store multiple items in a single variable.
# e.g thislist = ["apple", "banana", "cherry"]
# print(thislist)

# Q35. How can you create a list in Python?
# list can be created in [] square bracket, mylist = ["apple", "banana", "cherry"]

# Q36. How can we access the elements in a list?
# we can access list by chosing from list [0,1,2] according to what output we are wanted
# mylist = ["apple", "banana", "cherry"]
# print(mylist[0])

# Q37. Write a code to access the word "iNeuron" from the given list.
# ```
# lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
# print(lst[4][2])

# Q38. Take a list as an input from the user and find the length of the list.
# n=input("Enter the list ").split()
# print(len(n))

# Q39. Add the word "Big" in the 3rd index of the given list.
# ```
# lst = ["Welcome", "to", "Data", "course"]
# lst.insert(2,"Big")
# print(lst)

# Q40. What is a tuple? How is it different from list?
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, 
# and Dictionary, all with different qualities and usage.

# Tuple  is ordered and unchangeable.

# Q41. How can you create a tuple in Python?
# We have to use  round brackets () to work codes as a tuple otherwise python does not find this is a tuple or not
# tuplelist=("name",)
# print(tuplelist)
# output=('pawan', 'Dhuriya')

# Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.

# tuple are unchaged and immutable once created does not change.
# nametuple=(" ")
# nametuple.append('pawan')
# print(nametuple)

# Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
# Tuple is immutable, although you can use the + operator to concatenate several tuples. 
# s=('1','2',3)
# s_append=s+('4','5','6')
# print(s_append)

# Q44. Take a tuple as an input and print the count of elements in it.

# count=('2','apple','address','tree','travel')
# print(len(count))

# Q45. What are sets in Python?
# Sets are used to store multiple items in a single variable.

# Q46. How can you create a set?
   # we can create a set by using curly bracket {}.

# Q47. Create a set and add "iNeuron" in your set.
# set1={"iNeuron"}
# for x in set1:
#     print(x)

# Q48. Try to add multiple values using add() function.
# set1={"a","p","l","e"}
# set1.add('b')
# print(set1)

# Q49. How is update() different from add()?
# add() used to add one element to set. 
# update() method used to add multiple elements to set.

# Q50. What is clear() in sets?
# Here, set.clear() clears the set by removing all the elements of the set.
# number={'1','2','4',''}
# number.clear()
# print(number)

# Q51. What is frozen set?
# The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).

# Q52. How is frozen set different from set?
# Since the elements are fixed, unlike sets you can't add or remove elements from the frozen set.

# Q53. What is union() in sets? Explain via code.
# The union() method returns a set that contains all items from the original set, and all items from the specified set(s).
# Syntax: set1.union(set2, set3, set4….)
# set1 = {2, 4, 5, 6}
# set2 = {4, 6, 7, 8}
# x=set1.union(set2)
# print(x)

# Q54. What is intersection() in sets? Explain via code.
# The intersection() method returns a set that contains the similarity between two or more sets.
# A = {2, 3, 5}
# B = {1, 3, 5}
# print(A.intersection(B))
# print(B.intersection(A))

# Q55. What is dictionary in Python?
# Python dictionary is an ordered collection (starting from Python 3.7) of items.
# It stores elements in key/value pairs. Here, keys are unique identifiers that are associated with each value
# capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
# print(capital_city)

# Q56. How is dictionary different from all other data structures.
# A dictionary in data structure supports a wide variety of operations using a wide variety of methods and functions.
# The keys are always unique within a dictionary

# Q57. How can we delare a dictionary in Python?
# we can declare dictinoary in curly braces {}.Inside the curly braces you have a key-value pair. 
# Keys are separated from their associated values with colon, : .

# Q58. What will the output of the following?
# ```
# var = {}
# print(type(var))
# # ```<class 'dict'>

# Q59. How can we add an element in a dictionary?
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# Q60. Create a dictionary and access all the values in that dictionary.
# Countries = {
#     6:'Canada',
#     2:'United Kingdom',
#     1:'United States',
#     9:'Australia',
#     7:'China'
# }
# print(Countries.values())
# for value in Countries.values():
#     print(value)

# Q61. Create a nested dictionary and access all the element in the inner dictionary.
# dict={"name":{"f_name":"pawan","l_name":"d"},"age":29 ,"work":"iT" }
# for a,b in dict["name"].items():
#     print(f"the value {a},the secound value {b}")


# Q62. What is the use of get() function?
# The get() method returns the value of the item with the specified key.
# e.g dictionary.get(keyname, value)

# Q63. What is the use of items() function?
# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
# dictionary.items()

# Q64. What is the use of pop() function?
# The pop() method removes the element at the specified position.
# list.pop(pos)

# Q65. What is the use of popitems() function?
# The popitem() method removes the item that was last inserted into the dictionary.

# Q66. What is the use of keys() function?
# The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
# dictionary.keys()

# Q67. What is the use of values() function?
# Python dictionary values() function is used to return a new view object that contains a list of all the values associated with the keys in the dictionary


# Q68. What are loops in Python?
# A for loop is used for iterating over a sequence.

# Q69. How many type of loop are there in Python?
# 1)for Loop
# 2)while loop


# Q70. What is the difference between for and while loops?
# for loop is used to repetetive task again and agin perfroming untill loop value ended.
# for while loop the veriable value should be true or false according to it loop program excuted.

# Q71. What is the use of continue statement?
# continue:this statemnet is used to make loop or program running contiously.

# Q72. What is the use of break statement?
# break: is used to break the looping if we want to  break the progrma and exits.

# Q73. What is the use of pass statement?
# The pass statement is used as a placeholder for future code
# A pass statement signals to a loop that there is “no code to execute here.”

# Q74. What is the use of range() function?
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# range(start, stop, step)

# Q75. How can you loop over a dictionary?
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.



# ### Coding problems
# Q76. Write a Python program to find the factorial of a given number.
# num=int(input("enter the number: "))
# s=1
# if num>=0:
#       for i in range(1,num+1):
#         s=s*i 
# print(f"The factorial vaue is: ",s) 
   
# Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100
# def interset():
#     p=float(input(f"Enter the principal amount in rupee:- "))
#     r=float(input(f"Enter the rate of interset amount in %:- "))
#     t=int(input(f"Enter the time in year:- "))
#     SI=(p*r*t)/100      
#     print(f"the simple interset is: " ,SI)
# interset()   
#-----------------------------------
# Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.
# def  compond():
#     p=int(input(f"Enter the principal amount in rupee:- "))
#     r=float(input(f"Enter the rate of interset amount in %:- "))
#     t=int(input(f"Enter the time in year:- "))
#     A=0
#     A=p*(pow((1+r/100),t))
#     print(f"The compond interset is :- ",A)
# compond()
# Q79. Write a Python program to check if a number is prime or not.
# from math import sqrt
# n =int(input("Enter the number:- "))
# prime_flag = 0
 
# if(n > 1):
#     for i in range(2, int(sqrt(n)) + 1):
#         if (n % i == 0):
#             prime_flag = 1
#             break
#     if (prime_flag == 0):
#         print("this is a prime number")
#     else:
#         print("this is not a prime number")
# else:
#     print("this is  prime number")
   

# Q80. Write a Python program to check Armstrong Number.
# num = int(input("Enter a number: "))
# sum=0
# temp=num
# while temp>0:
#     a=temp%10
#     sum+=a**3
#     temp //=10
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")


# Q81. Write a Python program to find the n-th Fibonacci Number.
# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# for i in range(20):
#     print(fibo(i))


# Q82. Write a Python program to interchange the first and last element in a list.
# def interchnage(lst):
#     lst[0],lst[-1]= lst[-1],lst[0]
#     return lst
 
# lst=['i','n','e','u','r','o','n']
# # lst=[12, 35, 9, 56, 24]
# print(interchnage(lst))

# Q83. Write a Python program to swap two elements in a list.
# def swap(element):
#     element[4],element[2]=element[-1],element[3]
#     return element
# element=[1,2,3,4,5]
# print(swap(element))
    

# Q84. Write a Python program to find N largest element from a list.
# def largest(arr,n):
#     ans=max(arr)
#     return ans
# arr=[12,45,23,5,439,7,234,512,74,23,464]
# n=len(arr)
# print(f"largest number is ",largest(arr,n))          

# Q85. Write a Python program to find cumulative sum of a list.
# n=[10, 15, 20, 25, 30]
# lsum=0
# for i in range (len(n)):
#     lsum +=n[i]
#     print(lsum)


# Q86. Write a Python program to check if a string is palindrome or not.
# word=str(input("type word to be palindrome :- "))
# if word==word[::-1]:
#     print("This is palindrome word")
# else:
#     print("This is not palindrome word")

    

# Q87. Write a Python program to remove i'th element from a string.
# def element(string,i):
#     a=string[: i]
#     print(a)
#     b=string[i+1:]
#     print(b)
#     return a+b
# print(f"i'th elemnt is remove :",element(string="Ineuron",i=2))


# Q88. Write a Python program to check if a substring is present in a given string.
# def check_substring(s2, s1):
# 	if (s2.count(s1) > 0):
# 		print(f'"{s1}" is a substring of "{s2}"')
# 	else:
# 		print(f'"{s1}" is not a substring of "{s2}"')


# s2 = "Welcome to iNeuron Big Data Bootcamp"
# s1 = "iNeuron"
# check_substring(s2, s1)

# Q89. Write a Python program to find words which are greater than given length k.
# def string_check(string_length,my_string):
# 	result_string=[]
# 	words=my_string.split(" ")
# 	for x  in words:
# 		if len(x)>string_length:
# 			result_string.append(x)
# 	return result_string
# string_length=3
# my_string="Welcome to iNeuron Big Data Bootcamp "
# print(f"The string is :",my_string)
# print(string_check(string_length,my_string))

# Q90. Write a Python program to extract unquire dictionary values.
# dict1 = {'A' : [1, 3, 5, 4],
#              'B' : [4, 6, 8, 10],
#              'C' : [6, 12, 4 ,8],
#              'D' : [5, 7, 2]}

# print("The original dictionary is : " ,dict1)
  
# # Using list comprehension, values() and sorted()
# res = list(sorted({ele for val in dict1.values() for ele in val}))
  
# # print result 
# print("The unique values list is : " , res) 

# Q91. Write a Python program to merge two dictionary.
# def Merge(dict1, dict2):
#     res = {**dict1, **dict2}
#     return res
# dict1 = {'x': 10, 'y': 8}
# dict2 = {'a': 6, 'b': 4}
# dict3 = Merge (dict1, dict2)
# print(dict3)

# Q92. Write a Python program to convert a list of tuples into dictionary.
# ```
def convert(tup,di):
    di=dict(Input)
    return di
Input = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
dictionary={}
print(convert(Input,dictionary))
# Output = {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
# ```

# Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
# ```
# Input: 
list = [9, 5, 6]
res=[(val,pow(val,3))for val in list]
print(res)
# Output: [(9, 729), (5, 125), (6, 216)]
# ```

# Q94. Write a Python program to get all combinations of 2 tuples.
# ```
test_tuple1 = (7, 2) 
test_tuple2 = (7, 8)
res=[(a,b) for a in test_tuple1 for b in test_tuple2]
res=res+[(a,b)for a in test_tuple2 for b in test_tuple1]
print("Combination of tuples is :",str(res))

# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
# ```

# Q95. Write a Python program to sort a list of tuples by second item.
# ```
# Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
def Sort_Tuple(tup):
     
    lst = len(tup)
    for i in range(0, lst):
         
        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j]= tup[j + 1]
                tup[j + 1]= temp
    return tup
 
tup =[('452', 10), ('256', 5), ('100', 20), ('135', 15)]
       
print(Sort_Tuple(tup))
# Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
# ```

# Q96. Write a python program to print below pattern.
# n=int(input("Enter the value for start *: "))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end="")
#     print("\r")
# # ```
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# ```
# Q97. Write a python program to print below pattern.
# n=5;i=0
# while(i<=n):
#   print(" " * (n - i) +"*" * i)
#   i+=1
# ```
#     *
#    **
#   ***
#  ****
# *****
# ```

# Q98. Write a python program to print below pattern.
# n=9
# i=0
# while i<n:
#   print(' '*(n-i-1) + '* '* (i+1))   
#   i+=1

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# ```

# Q99. Write a python program to print below pattern.
# ```
# n=5
# for i in range(1,n+1):
#   for j in range(1,i+1):
#      print(j,end=" " )
#   print()    

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# ```

# Q100. Write a python program to print below pattern.
num=65
n=5
for i in range(0,n):
    for j in range(0,i+1):
        ch=chr(num)
        print(ch,end=" ")
    num=num+1
    print("\r")    
# ```
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
# ```