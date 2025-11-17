# Jarvis Bot :

# Website to generate API key: https://openrouter.ai/

import os
import json
import requests
import webbrowser
import pyttsx3 as ttsx
from pathlib import Path

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
        elif ("open instagram and search" in self.da) or ("open insta and search" in self.da) :
            if "instagram" in self.da :
                webbrowser.open (f"https://www.instagram.com/explore/tags/{self.da [26 : ]}/")
                speak (f"Instagram opening and searching for {self.da [26 : ]}")
            elif "insta" in self.da :
                webbrowser.open (f"https://www.instagram.com/explore/tags/{self.da [22 : ]}/")
                speak (f"Instagram opening and searching for {self.da [22 : ]}")
        elif ("open news and search" in self.da) or ("open new and search" in self.da) :
            if "news" in self.da :
                webbrowser.open (f"https://www.google.com/search?q=news+{self.da [21 : ]}")
                speak (f"News opening and searching for {self.da [21 : ]}")
            elif "new" in self.da :
                webbrowser.open (f"https://www.google.com/search?q=news+{self.da [20 : ]}")
                speak (f"News opening and searching for {self.da [20 : ]}")
        else :
            print ("Please enter valid command...")
            speak ("Please enter valid command...")
            
    def load_ai_key (self) :
        try :
            with open ("jarvis_ai_api.txt", "r") as f :
                content = f.read ().strip ()
            return content
        except Exception as e :
            api = cmd.write_api_key ()
            return api          

    def write_api_key (self) :
        req = input ("Do you have API key (Y/N) : ").lower ().strip ()
        if 'y' in req :
            data = input ("Enter your OpenRouter API key : ").strip ()
            with open ("jarvis_ai_api.txt", "w") as f :
                f.write (data)
            content = data
            print ("API key saved successfully and ready to use the chatbot features.")
            speak ("API key saved successfully and ready to use the chatbot features.")
            return content
        else :
            return False

    def ai_reply (self , data , content) :
        
        if len (content) > 70 :  
            API_KEY = content  # <-- Put your API key here safely !
            print("\nChatbot.\n")

            user_input = data
             
            body = {
            "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
            "messages": [
                {
                    "role": "system",
                    "content": "Give short, clear, smartest way and direct answers. Max 4 sentences."
                } ,
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        }

            try:
                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {API_KEY}",
                        "Content-Type": "application/json"
                    },
                    data=json.dumps(body)
                )

                result = response.json()

                if "choices" in result:
                    ai_reply = result["choices"][0]["message"]["content"]
                    print("AI :", ai_reply, "\n")
                    speak (ai_reply)  # Call the speak function to convert text to speech
                else:
                    print("AI Error :", result, "\n")
                    speak ("Sorry, I encountered an error while processing your request.")  # Speak error message.

            except Exception as e :
                print("Error :", e)

        else :
            print ("Your API key is invalid.")
            speak ("Your API key is invalid.")
            cmd.write_api_key ()
    
    def output (self) :
        speak ("Initializing Jarvis...")  
        speak ("Please enter the name of the assistant to activate it.")
        while True :
            print ("Please enter the name of the assistant to activate it : ")
            data = input ().lower ().strip ()
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
            data_2 = input ().lower ().strip ()

            if "search" in data_2 :
                cmd.websearch (data_2)
            elif "open" in data_2 :
                cmd.webprocess (data_2)
            elif ("exit" in data_2) or ('quit' in data_2) :
                print ("Thank you for using this program...")
                speak ("Thank you for using this program...")
                break
            else :
                api = cmd.load_ai_key ()
                if api == False :
                    print ("You need to get an API key from https://openrouter.ai/ to use the chatbot features.")
                    speak ("You need to get an API key from Open Router dot AI to use the chatbot features.")
                else :
                    cmd.ai_reply (data_2 , api)
                         
if __name__ == "__main__" :
    cmd = Command ()
    cmd.output ()

# The End.
