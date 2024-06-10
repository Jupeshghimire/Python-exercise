# Write a script called translate.py that asks the user for some input
# with the following prompt: Enter some text:. Then use the .replace()
# method to convert the text entered by the user into “leetspeak” by making the following changes to lower-case letters
# Theletter a becomes 4
# • Theletter b becomes8
# • Theletter e becomes3  
# Theletter l becomes1 
# • Theletter o becomes0 
# • Theletter s becomes5 
# • Theletter t becomes7

prompt=input("Enter some text \n" )
let_speak=prompt.lower()
let_speak=(let_speak.replace("a","4"))
let_speak=(let_speak.replace("b","8"))
let_speak=(let_speak.replace("e","3"))
let_speak=(let_speak.replace("l","1"))
let_speak=(let_speak.replace("o","0"))
let_speak=(let_speak.replace("s","5"))
let_speak=(let_speak.replace("t","7"))
print("The leetspeak translation is :\n",let_speak)