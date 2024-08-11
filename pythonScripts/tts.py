from TTS.api import TTS
import torch
import winsound
from rvc_python.infer import infer_file
import os
import time


class Model:
    def __init__(self,model = "tts_models/multilingual/multi-dataset/xtts_v2") -> None:
        self.type = "cuda" if torch.cuda.is_available() else "cpu"
        self.tts = TTS(model).to(self.type)
        print(f"Model created ({self.type})")

    def textToSpeech(self,text):
        self.tts.tts_to_file(text=text,file_path="mp3/output.wav",speaker_wav="cloning\welcome_to_the_internet_12pitch.wav",language="it",emotion="Sad")
        #self.tts.tts_to_file(text=text,file_path="mp3/output.wav",speaker_wav="cloning\yukiplayful_ohio.wav",language="it",emotion="Sad")
  
    def rvc(self):
        self.tts.voice_conversion_to_file(source_wav="mp3\output.wav",target_wav="cloning\welcome_to_the_internet_12pitch.wav",file_path="mp3/output1.wav")
        #self.tts.voice_conversion_to_file(source_wav="mp3\output.wav",target_wav="cloning\yukiplayful_ohio.wav",file_path="mp3/output1.wav")

        self.processVoiceChanger()
        
    def processVoiceChanger(self):

        result = infer_file(
    
            input_path=r"mp3/output1.wav",
            model_path=r"tts_models\Houshou Marine (Hololive) (TITAN)\Houshou_Marine.pth",
            index_path=r"tts_models\Houshou Marine (Hololive) (TITAN)\added_IVF405_Flat_nprobe_1_Houshou_Marine_v2.index",  # Optional: specify path to index file if available
            
            #model_path=r"tts_models\yuki_alt\yuki_alt.pth",
            #index_path=r"tts_models\yuki_alt\added_IVF375_Flat_nprobe_1_yuki_alt_v2.index",  # Optional: specify path to index file if available
            
            device="cuda", # Use cpu or cuda
            f0method="rmvpe",  # Choose between 'harvest', 'crepe', 'rmvpe', 'pm'
            f0up_key=0,  # Transpose setting
            opt_path=f"mp3/output2.wav", # Output file path
            index_rate=0.06,
            filter_radius=1,
            resample_sr=0,  # Set to desired sample rate or 0 for no resampling.
            rms_mix_rate=0.94,
            protect=0.4,
            version="v2"
        )
        winsound.PlaySound("mp3/output2.wav",winsound.SND_FILENAME)
        os.remove("mp3\output.wav")
        os.remove("mp3\output1.wav")
        os.remove("mp3\output2.wav")
        
        
        