#Ovozli yordamchi JarvisTag'o
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

#Barcha so'zlar jamlanmasi

opts={
    "alias": ("jarvistog`a", "jarvis", "joris", "joriy", "jarvistag`o", "jarviztog`a", "jarviztag`o", "jaris tog'a"),
    "tbr":("aytingchi", "ko`rsatchi", "ko`rsat", "necha", "aytchi", "aytingchi"),
    "cmds": {
        "ctime": ("hozirgi vaqt", "soat necha", "xozir vqat", "soat nechchi bo`ldi"),
        "radio": ("muzikani qo`y", "muzikani qo`yvoring", "radioni yoq"),
        "stupid1": ("latif aytib ber", "bitta zo`ridan bo`sin", "bitta yangisidan bo`sin")
    }
    
}
#Funksiyalar
def speak(what):
    print(what)
    speek_engine.say(what)
    speek_engine.runAndWait()
    speek_engine.stop()

def callback(recognizer, audio):
    try:
        voice=recognizer.recognize_google(audio, language="uz-Uz").lower()
        print("[log] Aytildi: " + voice)

        if voice.startswith(opts["alias"]):
            #Jarvistag`oga murojat
            cmd=voice

            for x in opts["alias"]:
                cmd=cmd.replace(x, "").strip()

            for x in opts["tbr"]:
                cmd=cmd.replace(x, "").strip()

            #Tekshiramiz va ishlatamiz
            cmd= recognizer_cmd(cmd)
            execute_cmd(["cmd"])
    except sr.UnknownValueError:
        print("[log] Shovqin qilmanglar eshitmayapman!")
    except sr.RequestError as e:
        print("[log] Shovqin kuchli bo`lyapti, ovoz eshitilmayapti!")





def recognizer_cmd(cmd):
    RC={"cmd": "", "": 0}
    for c, v in opts["cmds"].items():

        for x in v:
            vrt=fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC["cmd"]=c
                RC["percent"]=vrt

        return RC


def execute_cmd(cmd):
    if cmd=="ctime":
        #vaqtni ko`rsat
        now=datetime.datetime.now()
        speak("Hozirgi vaqt " + str(now.hour) + ":" + str(now.minute))

    elif cmd=="radio":
        #radioni yoqish
        os.system("C:\\Music\\AUD-20211127-WA0000")

    elif cmd=="stupid1":
        #Yemagan xazil
        speak("Bir kuni gugurt cho`p boshini qashiyman deb yonib ketipti!")


#ovoz
r=sr.Recognizer()
m=sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speek_engine=pyttsx3.init()
#Faqat biz yozgan ovozlarni!
voices=speek_engine.getProperty("voices")
speek_engine.setProperty("voice", voices[0].id)


#forced cmd test

speak("Salom MrUmidjan")
speak("Nima gaplar")

stop_listening=r.listen_in_background(m, callback)
while True:
    time.sleep(0.1)
