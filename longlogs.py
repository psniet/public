import time
import random
key = "epoch 1"
while(True):
    val = random.randint(0,9)    
    print(f"cnvrg_linechart_Regular key: {key} value: {val}")
    print(f"cnvrg_linechart_Scientific key: {key} value: {val}e-5")
    time.sleep(10)
