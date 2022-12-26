import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if len(rostos) > 0:
        return True, rostos
    return False, []

def rostos_conhecidos():
    rostos = []
    nomes = []

    foto1 = reconhece_face('img/felipe.jpg')
    if foto1[0]:
        rostos.append(foto1[1][0])
        nomes.append("Padrinho da 924")

    foto2 = reconhece_face('img/izabel.jpg')
    if foto2[0]:
        rostos.append(foto2[1][0])
        nomes.append("Izabel")
        
    marta = reconhece_face('img/marta.jpg')
    if marta[0]:
        rostos.append(marta[1][0])
        nomes.append("Marta")
        
    foto3 = reconhece_face('img/harry.jpg')
    if foto3[0]:
        rostos.append(foto3[1][0])
        nomes.append("Feio da 924")
        
    foto4 = reconhece_face('img/feto.jpeg')
    if foto4[0]:
        rostos.append(foto4[1][0])
        nomes.append("Ruan")
    
    return rostos, nomes
        