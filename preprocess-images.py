import numpy as np
import glob
from PIL import Image
import time

def main():
    startTime = time.perf_counter()
    malware = glob.glob("./images" + '/malware/*.png')
    goodware = glob.glob("./images" + '/goodware/*.png')

    for path in malware:
        print(path)
        localTime = time.perf_counter()
        img = Image.open(path).resize((128,128))
        img.save(path.replace("images", "processed-images", 1))
        print(time.perf_counter() - localTime)
        
    for path in goodware:
        print(path)
        localTime = time.perf_counter()
        img = Image.open(path).resize((128,128))
        img.save(path.replace("images", "processed-images", 1))
        print(time.perf_counter() - localTime)
        
    print(time.perf_counter() - startTime)

if __name__ == "__main__":
    main()
