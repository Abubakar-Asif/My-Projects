# Number Gussing Game :

from random import randint

rand = randint (1 , 100)
guss = 0

while True :
    try :
        guss += 1
        data = int (input ("Enter your guss : "))
        if (data < rand) and (data <= 100) :
            print ("Too Low.")
        elif (data > rand) and (data <= 100) :
            print ("Too High.")
        elif (data == rand) :
            print ("You gussed the right number.")
            break
        else :
            print ("Make sure you entered a number between 1 to 100.")
    except :
        print ("Make sure you entered a valid input.")

while True :
    try :
        with open ('number_guss_data.txt') as f :
            content = int (f.read ())
        if guss < content :
            with open ('number_guss_data.txt' , "w") as f :
                f.write (str (guss))
            print (f"Congrulation , you break the high score.")
            print (f"Previous high score {content}.")
            print (f"Your high score {guss}.")
            break
        else :
            print (f'Your score is {guss}.')
            break
    except :
        with open ('number_guss_data.txt' , "w") as f :
            f.write (str (guss))
        print (f"Your score is {guss}.")
        break

# The End.
