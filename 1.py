#1Write a program that IDLE won't rub because because it has syntax error.
#print("Hello world)

#2. Write a program that crashes only while running because it has run time error.
#print(Hello world)

#D3. isplay some text using print

print("wow")
print("Well done")

#4. ASSIGN A STRING TO  VARIABLE AND THEN PRINT THE CONTENT OF THE VARIABLE.
first_name = "Jupesh"
print(first_name)

print("")
print("")

#5. Print a string that uses double quotation inside string.
statement=('Issac Newtwon states that,"A body tends to stay at rest or motion unless an external force is applied"')
print(statement)
print('')
print("")
print("")

#6.Print a line that spans multiple lines with white preserved. 
Hello=""" Hello, it's me I was wondering if 
          after all this years you'd like to 
        meet.They said the time supposed to heal
        ya but I ain't done much a healing.
        """
print(Hello)
print("")
print("")
print("""

""")

#7.Print a string  that is coded on multi lines  but gets printed on a single line
argument=("Many scientist believe that the \
world is inhabited by other intellectual life froms too\
that's why we must be aware of our neighbouring galaxies.")
print(argument)
print("")
print("")
print("")


#8.Create a string and print it's length using len()
well=("I am you and you're me .")
print(len(well))
print("")
print("")

#9. Create two strings , concatenate them , and print the resulting string.
zip="1444"
nation="Nepal has the zip code:"
print(nation + zip) #No it doesn't.
print("")
print("")

#10. Create two strings , use concatenation to add space between and print the result

lip="Thy lips looks like cherry."
mole="The mole upon thy lips remid me of the star in the skies."
print(lip+" "+mole )

print("")
print("")
print()
#11.Print the string " zing " from the string " bazinga" using slicing
name102="bazinga"
print(name102[2:6])

print()
print(
)
print()

#12.Write a program that converts the following strngs to lowr case : "Animals","Badger","Honey Bee","Honey Badger".print each lower-case string on a seperate line.
lower_case=('"Animals"\n"Badger"\n"Honey Bee"\n"Honey Badger"')
print(lower_case.lower())
print()
print()
print()

#13.Write a program that converts the following strngs to uppercase: "Animals","Badger","Honey Bee","Honey Badger".print each upper-case string on a seperate line.
upper_case=('"Animals"\n"Badger"\n"Honey Bee"\n"Honey Badger"')
print(upper_case.upper())
print()
print()
print()

#14.Write  a program that removes white space from the following strings then prints out the string with the white space removed
#string1="    Fillet Mignon"
#string2="Brisket          "
#string3="  Cheeseburger     "
string1="    Fillet Mignon"
string2="Brisket          "
string3="  Cheeseburger     "
print(string1.strip())
print(string2.strip())
print(string3.strip())
print()
print()
print()

#15.Write a program  that prints out the result of a .startswith("be") on each of the following strings.
#string1= "Becomes"
#string2="becomes"
#string3="BEAR"
# #string4="bEautiful"
string_1= "Becomes"
string_2="becomes"
string_3="BEAR"
string_4="bEautiful"
print(string_1.startswith("be"))
print(string_2.startswith("be"))
print(string_3.startswith("be"))
print(string_4.startswith("be"))

print()
print()
print()
#16. SAME FOUR STRINGS OF EXERCISE 14 ,ALTER EACH STRING SO TAHT .startswith("be") returns true for all value.
string_1= "Becomes"
string_2="becomes"
string_3="BEAR"
string_4 = "bEautiful"
print(string_1.lower().startswith("be"))
print(string_2.lower().startswith("be"))
print(string_3.lower().startswith("be"))
print(string_4.lower().startswith("be"))

