import numpy as np
import statistics

def modefunction():
    sample = [1,3,2,4,5,6,7,7,5,7,8,4,1,3,1]
    print(statistics.mode(sample))

def medianfunction():
    sample = [1,3,2,4,5,6,7,7,5,7,8,4,1,3,1]
    print(statistics.median(sample))

def meanfunction():
    sample = [1,3,2,4,5,6,7,7,5,7,8,4,1,3,1]
    print(statistics.mean(sample))



meanfunction()
# medianfunction()
# modefunction()