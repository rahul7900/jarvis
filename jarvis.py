import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices)
# print(voices[0].id)
engine.setProperty("voices", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Jarvis, You artificial assistance!!!, Command me what to do?")


#  pip install speechRecognition
def takeCommand():
    # It take input as microphone and returns strings

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("hearing....")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    

    try:
        print("Give me a sec.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        # print(e)
        print("It was my bad , would you please repeat it")
        return "None"
    return query


# allow permisson of less_secure_email through your email
def sendEmail(content, to):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(
        "your_email", "your_password"
    )  # your_email is  your email && your_password is the password of gmail account
    server.sendmail(
        "sneder_email", to, content
    )  # sender_email is the email of person you want to send
    server.close()


if __name__ == "__main__":
    # speak("Rahul is a great guy")
    wishMe()
    takeCommand()
    while True:

        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia ....")
            query = query.replace("wekipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            # webbrowser.open("spotify.com")
            #             ||
            music_dir = "D:\\Non Critical\\songs\\Favorite Songs2"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is{strTime}")
        elif "open code" in query:
            codePath = "C:\\Users\\Rahul Singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "email to rahul" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "your_email@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!!!")
            except Exception as e:
                print(e)
                speak("Sorry Sir , I am not able to send email right now")
