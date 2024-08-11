import stt
import tts

model_1 = tts.Model("tts_models/multilingual/multi-dataset/xtts_v2")
model_2 = tts.Model("voice_conversion_models/multilingual/vctk/freevc24")

def faseDiAscolto():
    text = stt.getText()
    if text != "":
        model_1.textToSpeech(text=text)
        model_2.rvc()

def comunicazioneConBot():
    pass

while(True):
    faseDiAscolto() # Ha il suo tempo 
    comunicazioneConBot()
    
    
        