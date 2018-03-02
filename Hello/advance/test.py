#-*- coding:utf-8 -*-
'''
Created on 2018. 2. 23.

@author: lee
'''
from pip._vendor import requests
import time


import threading
 
def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
        time.sleep(0.001)
    print("Subthread", total)
 
t = threading.Thread(target=sum, args=(1, 100000))
t.start()
 
print("Main Thread")




