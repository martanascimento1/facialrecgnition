import speech_recognition as sr #pip install SpeechRecognition
import pyttsx3 #pip install pyttsx3
import datetime #pip install datetime
import wikipedia #pip install wikipedia
import pywhatkit #pip install pywhatkit

audio = sr.Recognizer()
maquina = pyttsx3.init()
maquina.say("Maria Izabel Lemos da SIlva!")
maquina.runAndWait()

'''def ouvindo_comandos():
  try:
     with sr.Microphone() as source:
        print("Ouvindo...")
        aud = audio.listen(source)
        comando = audio.recognize_google(aud, language="pt-BR")
        comando = comando.lower()
        print(comando)
        if "maria" in comando:
            comando = comando.replace("maria", "")
            print(comando)
            maquina.say(comando)
            maquina.runAndWait()
  except:
        print('Problema no microfone')

  return comando

def desejo_usuario():
    comando = ouvindo_comandos()
    if "apresente-se" in comando:
        maquina.say("Olá, meu nome é Maria e eu sou um código que foi desenvolvido para pedir que o professor Felipe Alencar para ser o padrinho da turma 924")
  
        maquina.runAndWait()
    elif "horas" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        maquina.say("Agora são "+hora)
        maquina.runAndWait()
    elif "procure por" in comando:
        procurar = comando.replace("procure por", "")
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif "toque" in comando:
        musica = comando.replace("toque", "")
        resultado = pywhatkit.playonyt(musica)
        print(resultado)
        maquina.say("Tocando música")
        maquina.runAndWait()

desejo_usuario()'''
        