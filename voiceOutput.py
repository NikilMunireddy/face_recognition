from gtts import gTTS
import os

def names_voice_output(name):
    textgiven=name
    tts=gTTS(text=textgiven)
    tts.save("Voice.aac")
    os.system("mpg321 Voice.aac")
    return 

name=input("name")
names_voice_output(name)
