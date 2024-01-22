import sounddevice as sd 
import numpy as np

threshold = 20
clap = False 

while user_input == y:
        def detect_clap(indata , frames , time , status):
            global clap 
            volume_norm = np.linalg.norm(indata)*10
            if volume_norm>threshold:
                print("Clapped!")
                clap = True
                user_input = input("Do you want to run this again? : y/n")
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
        //asking for input from user !! HAS BUGS !!
