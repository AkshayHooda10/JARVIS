import sounddevice as sd 
import numpy as np

threshold = 15
clap = False 

def detect_clap(indata , frames , time , status):
    global clap 
    volume_norm = np.linalg.norm(indata)*10
    if volume_norm>threshold:
        print("Clapped!")
        clap = True
    pass

def listen_for_clap():
    with sd.InputStream(callback=detect_clap):
        return sd.sleep(1000)

if __name__ == "__main__":
    while True:
        listen_for_clap()
        if clap == True:
            break
        else:
            pass