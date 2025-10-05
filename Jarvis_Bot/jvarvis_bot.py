# Jarvis Bot :

import webbrowser
import pyttsx3 as ttsx

def speak (text) :
    engine = ttsx.init ()
    engine.say (text)
    engine.runAndWait ()
    
class Command () :
    def webprocess (self , data) :
        self.data = data
        if "open google" in self.data :
            webbrowser.open ("http://www.google.com")
            speak ("Google opening...")
        elif "open youtube" in self.data :
            webbrowser.open ("http://www.youtube.com")
            speak ("YouTube opening...")
        elif "open facebook" in self.data :
            webbrowser.open ("http://www.facebook.com")
            speak ("Facebook opening...")
        elif "open instagram" or "open insta" in self.data :
            webbrowser.open ("http://www.instagram.com")
            speak ("Instagram opening...")
        elif "open news" in self.data :
            webbrowser.open ("http://www.news.com")
            speak ("News opening...")
        else :
            print ("Please enter valid command...")
            speak ("Please enter valid command...")
    def websearch (self , da) :
        self.da = da
        self.da.replace (" ", "+")
        if "open google and search" in self.da :
            webbrowser.open (f"https://www.google.com/search?q={self.da [23 : ]}")
            speak (f"Google opening and searching for {self.da [23 : ]}")
        elif "open youtube and search" in self.da :
            webbrowser.open (f"https://www.youtube.com/results?search_query={self.da [24 : ]}")
            speak (f"YouTube opening and searching for {self.da [24 : ]}")
        elif "open facebook and search" in self.da :
            webbrowser.open (f"https://www.facebook.com/search/top/?q={self.da [25 : ]}")
            speak (f"Facebook opening and searching for {self.da [25 : ]}")
        elif "open instagram and search" or "open insta and search" in self.da :
            if "instagram" in self.da :
                webbrowser.open (f"https://www.instagram.com/explore/tags/{self.da [26 : ]}/")
                speak (f"Instagram opening and searching for {self.da [26 : ]}")
            elif "insta" in self.da :
                webbrowser.open (f"https://www.instagram.com/explore/tags/{self.da [22 : ]}/")
                speak (f"Instagram opening and searching for {self.da [22 : ]}")
        elif "open news and search" or "open new and search" in self.da :
            if "news" in self.da :
                webbrowser.open (f"https://www.google.com/search?q=news+{self.da [21 : ]}")
                speak (f"News opening and searching for {self.da [21 : ]}")
            elif "new" in self.da :
                webbrowser.open (f"https://www.google.com/search?q=news+{self.da [20 : ]}")
                speak (f"News opening and searching for {self.da [20 : ]}")
        else :
            print ("Please enter valid command...")
            speak ("Please enter valid command...")
            
    def output (self) :
        speak ("Initializing Jarvis...")  
        speak ("Please enter the name of the assistant to activate it.")
        while True :
            print ("Please enter the name of the assistant to activate it : ")
            data = input ().lower ()
            if 'jarvis' in data :
                print ("Jarvis activate...")
                speak ("Jarvis activate...")
                print ("Hello sir , how may i assist you ?")
                speak ("Hello sir , how may i assist you ?")
                break
            else :
                print ("Make sure you activate the assistant before enter the command.")
                speak ("Make sure you activate the assistant before enter the command.")

        while True :
            data_2 = input ().lower ()
            if "search" in data_2 :
                cmd.websearch (data_2)
            elif "open" in data_2 :
                cmd.webprocess (data_2)
            elif ("exit" in data_2) or ('quit' in data_2) :
                print ("Thank you for using this program...")
                speak ("Thank you for using this program...")
                break
            else :
                print ("Please entered valid command.")
                speak ("Please entered valid command.")
        
if __name__ == "__main__" :
    cmd = Command ()
    cmd.output ()
     
# The End.
