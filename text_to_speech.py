import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import time
from gtts import gTTS
from pydub import AudioSegment
import pygame

def speak(text):
    language = "en"
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")

    audio = AudioSegment.from_mp3("output.mp3")
    audio.export("output.wav", format="wav")

    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

    os.remove("output.mp3")
    os.remove("output.wav")