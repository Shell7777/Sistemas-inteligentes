import speech_recognition as sr

r = sr.Recognizer()
def voz_number():
    with sr.Microphone() as source:
        while True:
            try:
                print("Di algo....")
                r.adjust_for_ambient_noise(source)
                audio = r.record(source, duration=3)
                text = r.recognize_google(audio)
                t = "{}".format(text)
                if (t=='one'):
                    number_speaker = 1 
                if (t=='two'):
                    number_speaker = 2 
                if (t=='three'):
                    number_speaker = 3 
                if (t=='for'):
                    number_speaker = 4 
                if (t=='five'):
                    number_speaker = 5 
                if (t=='six'):
                    number_speaker = 6 
                if (t=='seven'):
                    number_speaker = 7 
                if (t=='height'):
                    number_speaker = 8 
                if (t=='nine'):
                    number_speaker = 9 
                if (t=='ten'):
                    number_speaker = 10 
                print (t)
                print (number_speaker)
            
            except:
                print("error al escuchar")
voz_number()                