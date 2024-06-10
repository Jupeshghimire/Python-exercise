#25. In one line of code, display the result of trying to .find() the substring "a" in the string "AAA". The result should be -1
a_string="AAA"
print(a_string.find("a"))
print()
print()

# 26 Replace every occurrence of the character "s" with "x" in the string
# "Somebody said something to Samantha."

statement="Somebody said something to Samantha."
print(statement.replace("s","x"))
print()

#27.Write and test a script that accepts user input using the input()
# function and displays the result of trying to .find() a particular
# letter in that input
user_1input=input("Please enter a desire script\n")
display_user=input("Please enter the desired word from the script to be found : \n")
i=user_1input.find(display_user)
if  i == -1:
    print(f"The given word {display_user} is not found in {user_1input} ")
else:
    print(f"The given word {display_user} is in the script {user_1input}")
print(i)
print()
print(
)

 #28. Write a script that asks the user to input a number and then dis- 
 # plays that number rounded to two decimal places. When run, your program should look like this:
# Enter a number: 5.432
# 5.432 rounded to 2 decimal places is 5.43
num=(float(input("Enter a number:\n")))
print(f"{num} rounder to 2 decimal places is {round(num,2)}")
print()

#29. Writeascriptthataskstheusertoinputtwonumbersbyusingthe 
# input() function twice, then display whether or not the difference between those two number is an integer. When run, your program
# should look like this:
# Enter a number: 1.5
# Enter another number: .5
# The difference between 1.5 and .5 is an integer? True!
# If the user inputs two numbers whose difference is not integral, the output should look like this:
# Enter a number: 1.5
# Enter another number: 1.0
# The difference between 1.5 and 1.0 is an integer? False!

integer1=(float(input("Enter a number :  ")))
integer2=(float(input("Enter another number :  ")))
diff_int=(integer1 - integer2)
if diff_int %1==0:
  print(f"The difference between {integer1} and {integer2} is an integer? True! ")
else:
    print(f"The difference between {integer1} and {integer2} is an integer? False! ")

# 30. Print the result of the calculation 3 ** .125 as a fixed-point number with three decimal places.
first_num=3
second_num= .125
power= first_num ** second_num
print(f"{first_num} to the power of {second_num} is {power:.3f}")
print()

#31.Print the number 150000 as currency, with the thousands grouped with commas.
#  Currency should be displayed with two decimal places.

dollar=150000
print(f"I have an annual income of {dollar:,.2f}")
print()

#32. Print the result of 2 / 10 as a percentage with no decimal places.
#  The output should look like 20%.
dec=2 
imal=10
decimal=dec / imal
print(decimal)
print(f"I have {decimal:.1%}  share in the World bank.")

#32.