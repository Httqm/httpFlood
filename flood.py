#!/usr/bin/env python3

from multiprocessing import Process
import http.client
import os
import sys
import time

httpHost    = '192.168.1.8'
httpMethod  = 'GET'
httpQuery   = '/'

nbProcesses = 2
sleepDurationSeconds = 1


def floodHttpRequests(httpHost, httpMethod, httpQuery):
    processPid = os.getpid()
    conn       = http.client.HTTPConnection(httpHost)
    count      = 0
    increment  = 10

    while(True):
        notCacheableHttpQuery = httpQuery + '?%s%s' % (processPid, count)
#        print(notCacheableHttpQuery)

        try:
            conn.request(httpMethod, notCacheableHttpQuery);
            resp = conn.getresponse();
            resp.read();
            count += 1
            if not processId:               # let only the process 0 display stats...
                if(count % increment == 0): # ... every 'increment' loops
                    print("%s x %s = %s requests sent" % (nbProcesses, count, nbProcesses * count))

        except KeyboardInterrupt:
            print("\t[process %s] : interrupted by CTRL-c\n" % processId)
            sys.exit(42)

        time.sleep(sleepDurationSeconds)


for processId in range(nbProcesses):
    newProcess = Process(
        target = floodHttpRequests,
        args   = (httpHost, httpMethod, httpQuery)
        )
    newProcess.start()








