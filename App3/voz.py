import speech_recognition as sr

r = sr.Recognizer()
def voz_number(text_number):
    print ('Ingresa tu edad:')
    edad = int(input(''))
    R1 = text_number * edad
    with sr.Microphone() as source:
        while True:
            try:
                print("Di algo....")
                r.adjust_for_ambient_noise(source)
                audio = r.record(source, duration=3)
                text = r.recognize_google(audio)
                t = "{}".format(text)
                print (t)
                print (f'{text_number} X {edad} = {R1}')
                print ('NUMERO HABLADO',t )
                print ('R1',R1 )
                t = f'{t}'
                R1 = f'{R1}'
                resultado = 'Son iguales' if  R1==t  else 'No son iguales'
                print (resultado)
            
            except:
                print("error al escuchar")
                