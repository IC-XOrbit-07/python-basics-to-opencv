# Day 1: Revising Python Basics 

# Python is a dynamic(variable example) and strongly typed(5+"10" gives error) language 

# Printing Hello World => This is a single line comment also
print("Hello World") # (No need to end any line in python with ';' or ':')

'''
This is a multi line comment in python
You can also write comment here
Even here also 

'''

# Variables 
height = 182                                                            # int variable  
weight = 72.5                                                           # double/float variable 
name = "Chinmay"                                                        # string variable
multi_line_string = ''' This is a multi line string  
        this can go here also '''                                       # Multiline String variable

# Arithmetic Operations
print("Floor Division (12//5)        = ", 12//5)                        # `//` is a floor division (also called integer division)
print("True Division  (12/5)         = ", 12/5)                         # / is a float division operator (also known as true division).


# Printing in same line 
print("Same Line Print 1             : ", end = "", sep="SEP_VALUE")    # Pass value in end = "" to repeat it after every string
print("Same Line Print 2")                                              # Use `end=""` to keep both prints on the same line
print("Repeated String (Loop*10)     : " + "Loop"*10)                   # To print any string n number of times


print()                                           # Empty Seperator Line Print


print("--------------------------------------------------List Start--------------------------------------------------")

# List (Mutable Data Type)

colleges_list = ["CU", "IIT", "NIT", "IIIT"]                            # Declaring a list with 4 string elements
print("College List                  : ",colleges_list)
print("Accessing Index 0             : ", colleges_list[0])             # Access element at index 0 using colleges_list[index]       
colleges_list[0] = "Chandigarh University"                              # Update element at index 0 by assigning new value
print("After Updating Index 0        : ", colleges_list)                           

# List Funtions 
print("Slicing [1:3]                 : ", colleges_list[1:3])           # Slicing returns elements from index 1 to 2 (end index is exclusive)         
colleges_list.append("Another Colleges")                                # append() adds new element at the END of the list
print("After Appending               : ", colleges_list)                             
colleges_list.insert(2, "New")                                          # insert(index, value) adds element at the given index, shifts rest right
print("After Inserting at Index 2    : ", colleges_list)                             
colleges_list.remove("IIIT")                                            # remove(value) removes the FIRST occurrence of the given value
print("After Removing 'IIIT'         : ", colleges_list)                             
print("Length of List                : ", len(colleges_list))           # len() returns total number of elements in the list       
print("Max (Last Alphabetically)     : ", max(colleges_list))           # max() returns element that comes last alphabetically (lexicographic order)            
print("Min (First Alphabetically)    : ", min(colleges_list))           # min() returns element that comes first alphabetically (lexicographic order)

print("---------------------------------------------------List End---------------------------------------------------")

print()                                           # Empty Seperator Line Print

print("-------------------------------------------------Tuples Start-------------------------------------------------")

# Tuples (Immutable Data Type)

colleges_tuple = ("CU", "IIT", "NIT", "IIIT")                           # Tuple of College Name in string
print("College Tuple                 : ",colleges_tuple)
print("Accessing Index 0             : ", colleges_tuple[0])                          
# colleges_tuple[0] = "Chandigarh University"                           # Gives Error because tuples is immutable 

# Tuple Funtions 
print("Slicing [1:3]                 : ", colleges_tuple[1:3])                        
# colleges_tuple.append("Another Colleges")                             # Not Possible in tuple because of immutable nature
# colleges_tuple.insert(2, "New")                                       # Not Possible in tuple because of immutable nature  
# colleges_tuple.remove("IIIT")                                         # Not Possible in tuple because of immutable nature
print("Length of Tuple               : ", len(colleges_tuple))          # len() returns total number of elements in the tuple            
print("Max (Last Alphabetically)     : ", max(colleges_tuple))          # max() returns element that comes last alphabetically (lexicographic order)              
print("Min (First Alphabetically)    : ", min(colleges_tuple))          # min() returns element that comes first alphabetically (lexicographic order)               

print("--------------------------------------------------Tuples End--------------------------------------------------")

print()                                           # Empty Seperator Line Print

print("--------------------------------------------------Dict Start--------------------------------------------------")

# Dictionary (Key Value Pair, Mutable data type)

names = {
    "Chinmay": 22,
    "Kriti": 24,
    "Himanshu": 21
} 

print("Printing Dictionary           : ", names)                        # Prints entire dictionary with all key-value pairs                  
print("Accessing Key 'Chinmay'       : ", names["Chinmay"])             # Access value using its key inside square brackets
names['Chinmay'] = 23                                                   # Update value of existing key by assigning new value       
print("After Updating 'Chinmay' -> 23: ", names)                                      
names["Tanish"] = 10                                                    # Add new key-value pair if key doesn't exist
print("After Adding 'Tanish' -> 10   : ", names)

print("--------------------------------------------------Dict End---------------------------------------------------")

print()                                           # Empty Seperator Line Print

print("--------------------------------------Input & If-else Statement Start----------------------------------------")


# number = input()                                                        # Take string input by default  (type = <class 'str'>)
# print("Enter value to see range: ", end="")
# number_input = int(input())                                             # Takes int input               (type = <class 'int'>)
number = 99
if number>=90:
        print("You are in the range of >= 90 (hardcoded value = 99)")
elif number>=60:
        print("You are in the range of [60-90)")
else:
        print("You are not eligible for anything here")

print("--------------------------------------Input & If-else Statement End-----------------------------------------")

print()                                           # Empty Seperator Line Print

print("-------------------------------------------------Loop Start--------------------------------------------------")

# ---------- FOR LOOP ----------
print("DEMONSTRATING FOR LOOP")
n = 10
for i in range(0, n):
    print(i, end=" ")

# ---------- FOR-EACH LOOP ----------
print("\n\nDEMONSTRATING FOR EACH LOOP")
list1 = ['Element 1', 'Element 2', 'Element 3']
for item in list1:
    print(item)

# ---------- WHILE LOOP ----------
print("\nDEMONSTRATING WHILE LOOP")
print("Enter while loop value: ", end="")
while_number = 4

while while_number != -1:
    print("| i = ", while_number, " |")
    while_number -= 1
    if while_number == 0:
        print("Reached Zero")
        break
    
print("-------------------------------------------------Loop End---------------------------------------------------")

print()

print("----------------------------------------------Function Start------------------------------------------------")

param1 = 100
param2 = 200

def my_function_name(param1, param2):                                     # Defining function using def keywork & passing parameters
       return param1+param2*10                                                   

print(my_function_name(param1, param2))                                   # Calling function & passing argument to it

print("----------------------------------------------Function End--------------------------------------------------")

print()

print("----------------------------------------------Strings Start-------------------------------------------------")

string1 = "This is a string"

print("String is                    :", string1)
print("Index from 0 to 2            :", string1[0:3])                     # Slicing String (index => [0,3))  
print("Print last 2                 :", string1[-2:])                     # 2 Characters from back
print("Print all execpt last 2      :", string1[:-2])                     # Print whole except last 2 char
print("Capitalize first char        :", string1.capitalize())             # To Capitalize first char of string
print("First Occurrence of this     :", string1.find("thsdis"))           # To find starting index of a substr (-1 if not present)
print("To replace This with That    :", string1.replace("This", "That"))  # To replace all occurrence with another part

print("-----------------------------------------------Strings End--------------------------------------------------")
