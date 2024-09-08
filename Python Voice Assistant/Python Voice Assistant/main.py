import speech_recognition as sr 
import webbrowser
import pyttsx3  
import musicLibrary
import requests

#pip install pocketsphinx and google sr

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "c8320e29b762415a9a065c28a1603ab5"

def speak(text):
    engine.say(text)
    engine.runAndWait()
        
def process_command(c):
    if "open brave" in c.lower():
        webbrowser.open("https://brave.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com") 
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com") 
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
 
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=ina&apiKey=c8320e29b762415a9a065c28a1603ab5")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
 
            # Extract the articles
            articles = data.get('articles', [])        

            # Print the headlines
            for article in articles:
               speak(article['title'])

if __name__ == "__main__":
    speak("Initializing Zara....")
    print("Initializing Zara...")
    while True:
        # Listen for the wake word "zara"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "zara"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Zara Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    process_command(command)

        except Exception as e:
            print("Error; {0}".format(e))  

