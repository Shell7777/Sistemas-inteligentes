# * cv2 : deteccion de movimientos, reconocimeintos de objketos
import cv2, PIL 

# numpy : manejo de imagenes a trtaves matris de pixels
import numpy as np

# Operaciones matriciales y grafivcos 
#Para el reconocimiento de imagernes con patrones Aruco
from cv2 import aruco

# Colleccion de funciones de estilo de comando que hace matplottlib  
import matplotlib.pyplot as plt 

# Controlador para servicio de reconocimeinto de voz
import speech_recognition as sr

img1 = cv2.imread('butterfree.jpg')
img2 = cv2.imread('butterfree.jpg')


r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print ('Di algo..')
        r.adjust_for_ambient_noise(source)
        audio = r.record(source,duration=3)
        try:
            text = r.recognize_google(audio)
            t = "{}".format(text)
            if (t=="game"):
                print("Iniciando Reconocimienot de marcadores Aruco")
                cap = cv2.VideoCapture(0)
                while True :
                    _, frame  = cap.read ()
                    gray = cv2.cvtColor(frame,cv2.COLOR_BRG2GRAY)
                    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
                    parameters  = aruco.DetectorParameters_Create()
                    corners,ids, rejectImpPoints = aruco.detecMakers(gray,aruco_dict,parameters=parameters) 
                    frame_markers = aruco.drawDetectMarkers(frame,corners,ids)
                    print(corners)
                    if ids != None:
                        if ids[0][0] == 0 :
                            s_img = img1
                            x = corners[0][0][0][0]
                            y = corners[0][0][0][1]
                            print(x)
                            print(y)
                            frame[0:s_img.shape[0],0:s_img.shape[1]] = s_img
                        if ids[0][0] == 50 :
                            s_img = img2
                            x = corners[0][0][0][0]
                            y = corners[0][0][0][1]
                            print(x)
                            print(y)
                            frame[0:s_img.shape[0],0:s_img.shape[1]] = s_img
                    cv2.imshow ('Frame',frame )
                    key = cv2.waitKey(1)
                cap.release()
                cv2.destroyAllWindows()    

        except:
            print('Hubo un error al escuchar el audio')