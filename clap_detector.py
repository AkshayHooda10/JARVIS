import sounddevice as sd 
import numpy as np

threshold = 20
clap = False 
user_input = 'y'

        def detect_clap(indata , frames , time , status):
            global clap, user_input 
            volume_norm = np.linalg.norm(indata)*10
            if volume_norm>threshold:
                print("Clapped!")
                clap = True
                user_input = input("Do you want to continue this program : y/n ?")

        def listen_for_clap():
            with sd.InputStream(callback=detect_clap):
                return sd.sleep(1000)
                
        if __name__ == "__main__":
            while user_input.lower()=='y':
                clap = False
                listen_for_clap()
                if clap == True:
                    break
            
        
