import numpy as np
import face_recognition as fr
import cv2
from controlador import rostos_conhecidos
import webbrowser
import time

rostos, nomes = rostos_conhecidos()

webcam = cv2.VideoCapture(0)
while True:
    verificador, frame = webcam.read()
    rgb_foto = frame[:, :, ::-1]

    face_localizaco = fr.face_locations(rgb_foto)
    face_encodings = fr.face_encodings(rgb_foto, face_localizaco)

    for (emcima, direita, embaixo, esquerda), face_encodings in zip(face_localizaco, face_encodings):
        resultado = fr.compare_faces(rostos, face_encodings)
        print(resultado)
        
        distancia_faces = fr.face_distance(rostos, face_encodings)

        melhor_id = np.argmin(distancia_faces)
        if resultado[melhor_id]:
            nome = nomes[melhor_id]
        else:
            nome = "Desconhecido"
        
        cv2.rectangle(frame, (esquerda, emcima), (direita, embaixo), (200, 200, 200), 2)
        
        cv2.rectangle(frame, (esquerda, embaixo - 35), (direita, emcima), (200, 200, 200), 3)
            
        fonte_texto = cv2.FAST_FEATURE_DETECTOR_THRESHOLD
        cv2.putText(frame, nome, (esquerda + 6, embaixo - 6), fonte_texto, 1.0, (255, 255, 255), 1)

        cv2.imshow("Reconhecimento facial", frame)
    if cv2.waitKey(5) == 27:
        break
    
if nome == "Padrinho da 924":
        webbrowser.open("file:///home/marta/%C3%81rea%20de%20Trabalho/reconhecimento/index.html")

webcam.release()
cv2.destroyAllWindows()