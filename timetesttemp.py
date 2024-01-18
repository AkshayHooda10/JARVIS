import time
start_time = time.time()
duration = 3
while time.time() - start_time < duration :
    print("Hi")
    time.sleep(1)