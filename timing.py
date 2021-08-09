import os
import time
t1 = time.time()
#os.system("python detect.py --save-txt --save-crop --save-conf --source wtc.mp4")
os.system("python detect.py --device 0 --source ../mit/output_frames")
t2 = time.time()
print("Time Elapsed = ",t2-t1)

