#!/usr/bin/python

/* creates 10 threads and each thread sends 1k request each to the server

import requests
import threading

threadCount = 10
requestCount = 1000
serverUrl = "http://mysite.com"

def httpCall(threadName):
    for x in range(0, requestCount):
        response = requests.get(serverUrl)
        print(response.text + "    Thread Id = " + threadName)


for x in range(0, threadCount):
    t1 = threading.Thread(target=httpCall, args=(str(x))).start()

