# Central Library App :

import pyttsx3 as ttsx

def speak (text) :
    engine = ttsx.init ()
    engine.say (text)
    engine.runAndWait ()

class Book :
    def __init__(self , book):
        self.book = book
        self.lis = book.split ('\n')
    
    def list_books (self) :
        print ("The books are available in the library are :")
        speak ("The books are available in the library are :")
        a = 1
        for i in self.lis :
            print (f"{a}. {i}")
            speak (f"{a}. {i}")
            a += 1

    def Borrow (self) :
        speak ("Enter the name of the book you want to borrow.")
        data = input ("Enter the name of the book you want to borrow : ").title ().strip ()
        if data in self.lis :
            print (f"You have borrowed a {data} book from the library , please keep it safe and return within 30 days.")
            speak (f"You have borrowed a {data} book from the library , please keep it safe and return within 30 days.")
            self.lis.remove (data)
            with open ("Central_Library_File.txt" , "w") as f :
                f.write ("\n".join (self.lis))
        else :
            print (f"The {data} book is not currently available in the library , please wait until the book is available.")
            speak (f"The {data} book is not currently available in the library , please wait until the book is available.")
    
    def Return (self) :
        speak ("Enter the name of the book you want to return.")
        data = input ("Enter the name of the book you want to return : ").title ().strip ()
        if data in self.lis :
            a = 1
            while True :
                a += 1
                b = str (a)
                c = data + " " + b
                if c in self.lis :
                    continue
                else :
                    print (f"Thank you for returning the {c} book to the library.")
                    speak (f"Thank you for returning the {c} book to the library.")
                    with open ("Central_Library_File.txt" , "a") as f :
                        f.write ("\n" + c)
                    break
                    
        elif data not in self.lis :
            print (f"Thank you for returning the {data} book to the library.")
            speak (f"Thank you for returning the {data} book to the library.")
            with open ("Central_Library_File.txt" , "a") as f :
                f.write ("\n" + data)
    def Search (self) :
        speak ("Enter the name of the book you want to search.")
        data = input ("Enter book name : ").title ().strip ()
        if data in self.lis :
            print (f"{data} book is available in the library.")
            speak (f"{data} book is available in the library.")
        else :
            print (f"{data} book is not currently available in the library.")
            speak (f"{data} book is not currently available in the library.")
            
if __name__ == "__main__" :
    library = '''Python
Java
C
C ++
Java Script'''
    intro_txt = '''********** Welcome To The Central Library **********
Please Choose An Option :
1. List all available books.
2. Borrow a book.
3. Return a book.
4. Exit the program.
5. Search a book.'''
    intro_speak = '''Welcome to the central library :
Please choose an option :
press 1 to list all available books in the library.
press 2 to borrorw the book from the library.
press 3 to return the book to the library.
press 4 to exit the program.
press 5 to search a book.'''

    print (intro_txt)
    speak (intro_speak)

    while True :
        try :
            try :
                with open ("Central_Library_File.txt") as f :
                    content = f.read ()
            except :
                with open ("Central_Library_File.txt" , "w") as f :
                    f.write (library)
                    continue
            book = Book (content)           
            ch = int (input ("Enter your chooice : "))
            if ch == 1 :
                book.list_books ()
            elif ch == 2 :    
                book.Borrow ()
            elif ch == 3 :    
                book.Return ()
            elif ch == 4 :
                print ("Thank you for using this program.")
                speak ("Thank you for using this program.")
                break
            elif ch == 5 :
                book.Search ()
            else :
                print ("Make sure you entered a number between 1 to 4.") 
                speak ("Make sure you entered a number between 1 to 4.")

        except ValueError :    
            print ("Make sure you entered a number not alphabets.")
            speak ("Make sure you entered a number not alphabets.")

# The End.
