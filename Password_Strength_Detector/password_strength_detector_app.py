# Password Srength Detector Application :

import string as st
import random as rand
import pyttsx3 as ttsx

def speak (text) :
    engine = ttsx.init ()
    engine.say (text)
    engine.runAndWait ()

def check_password (data , suggestion) :
    score = 0
    if len (data) >= 8 :
        score += 1
    else :
        suggestion.append ("Your Password is too short , your password should be at least 8 characters long.")
    if any (da.islower() for da in data) :
        score += 1
    else :
        suggestion.append ("Add Lowercase Letters.")
    if any (da.isupper () for da in data) :
        score += 1
    else :
        suggestion.append ("Add Uppercase Letters.")
    if any (da.isdigit () for da in data) :
        score += 1
    else :
        suggestion.append ("Add Numbers.")
    if any (da in special_char for da in data) :
        score += 1
    else :
        suggestion.append ("Add Special Characters.")
    return score

def password_suggestion (suggestion) :
    print ("Suggestions for a strong Password :")
    speak ("Here are some suggestion for you to create a strong password.")
    for i in suggestion :
        print ("- " + i)
        speak ("- " + i)

def result (data) :
    if data <=2 :
        return "Your Password strength is Weak."
    elif data <= 4 :
        return "Your password strength is Medium."
    else :
        return "Your password strength is strong."

special_char = st.punctuation
lower_case = st.ascii_lowercase
upper_case = st.ascii_uppercase
digits = st.digits
strong = lower_case + upper_case + digits + special_char
suggestion = []
print ("Welcome To The Password Strength Detector.")
speak ("Welcome To The Password Strength Detector.")

speak ("Enter your password to check your password strength.")
while True :
    data = input ("Enter your password : ")
    strength = check_password (data , suggestion)
    output = result (strength)
    if (data.lower () == 'exit') or (data.lower () == 'quit') :
        print ("Thankyou for using this app , Have a great day ahead.")
        speak ("Thankyou for using this app , Have a great day ahead.")
        break
    elif data.lower () == 'generate' :
        password = "".join (rand.choices (strong , k=11))
        print ("Suggested Password :\n" + password)
        speak ("Here are a suggested password for you which are given below :")
        speak (password)
    elif suggestion != [] :
        print (output)
        speak (output)
        password_suggestion (suggestion)
        suggestion = []
    else :
        print (output)
        speak (output)

# The End.
