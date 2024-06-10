# #17.Write a program that takes input from the user and displays that input back

starting_convo=input("How was your day ? ")
print("Damn! really?" + starting_convo )
print()
print()

# #18.Write a program that takes input from the user and displays the input in lower case
name=input("What's your name ? ")
lower_name=name.lower()
print("Nice to meet you , "+lower_name )
print()
print()

#19.Write a program that takes input from the user and displays the number of character in the input.

last_name=input("What's your last name again ?? ")
last=str(len(last_name))
print("Damn your last name has "+ last + " characters ")
print()
print()

#20.Create a string containing an integer, then convert 
# that string into
# an actual integer object using int().
#  Test that your new object is
# a number by multiplying it by another
#  number and displaying the
# result.

just_fire= "17"
just_fire = int(just_fire)
double_fire =(2 * just_fire)
print(double_fire)
print(type(double_fire))
print()
print()

 #20. Repeat the previous exercise,
#  but use a floating-point number and
# float().
just_ice = "13.565"
just_ice=float(just_ice)
print(type(just_ice))
double_ice=2 * just_ice
print(double_ice)
print(isinstance(double_ice,float))
print()
print()

# 21 .Create a string object and an integer object
# , then display them side
# by side with a single print statement using str().
address="I live in "
street_code=23
print(address + str(street_code)+"rd"+ " street")
print()
print()
print()

#22.  Write a program that uses input() 
# twice to get two numbers from
# the user, multiplies the numbers together
# , and displays the result.
# If the user enters 2 and 4,
#  then your program should print the
# following text:
# The product of 2 and 4 is 8.0

num1=input("Please enter the first number :\n ")
num2=input("Please enter the second number:\n ")
# sum_num= float(num1) * float(num2)
print(f"The product of {num1} and {num2} is {float(num1) * float(num2)}")
# print("The product of "+ str(num1) + " and " +  str(num2) +" is " + str(sum_num) )\
print(
)
print()
print()

# 22. Create a float object named weight with the value 0.2, and create
# a string object named animal with the value "newt". Then use these
# objects to print the following string using only string concatenation:
# 0.2 kg is the weight of the newt.
weight=0.2
animal="newt"
print(str(weight)+" kg is the weight of the " + animal + ".")
print()
print()
print()


#23. Display the same string by using .format() and empty {} placeholders.
weight =0.2
animal = "newt"
print("{} kg  is the weight of the {}.".format(weight,animal))
print()
print()
print()

#24. Display the same string using an f-string.
weight=0.2
animal= "newt"
print(f"{weight} kg is the weight of the {animal} ")
print()

#25.   Write a script that asks the user to input a number and then dis-
# plays the absolute value of that number. When run, your program
# should look like this:
# Enter a number: -10
# The absolute value of -10 is 10.0

abs_num=float(input("Enter a number:\n"))
print(f"The absoluter value of {int(abs_num)} is {abs(abs_num)}")

# Writeascriptthataskstheusertoinput two numbersbyusingthe input()
#  function twice, then display whether or not the difference between those two number is an integer. When run, your program
# should look like this:
# Enter a number: 1.5
# Enter another number: .5
# The difference between 1.5 and .5 is an integer? True!
# If the user inputs two numbers whose difference is not integral, the output should look like this:
# Enter a number: 1.5
# Enter another number: 1.0
# The difference between 1.5 and 1.0 is an integer? False!

integer1=float(input("Enter a number :  "))
integer2=float(input("Enter another number :  "))
diff_int=integer1 - integer2
# if diff_int == type(int):
print(f"The difference between {integer1} and {integer2} is an integer? {isinstance(diff_int)} ")