#Write a program named first_letter.py that prompts the user for input with the string /
# "Tell me your password:". The program should then determine the ﬁrst letter of the user’s input, convert that letter to uppercase, and display it back.
login_password=input("Tell me you password:\n")
comp_answer="Oh your password has first letter:\n  "
if login_password:
     print(comp_answer + login_password[0].upper())
else:
     print("You didn't press any thing ")

