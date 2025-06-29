#!/usr/bin/env python3

import datetime
import math
import os
import sys
import time

if(len(sys.argv) < 2 ):
	print("usage: simulation.py <integer>\n")
	exit(1)

print(datetime.datetime.now().strftime('Starting %Y %d %b %H:%M:%S\n'))
text = input("Please enter some text: ");
print('The input contains: %s\n' % text)
os.system("echo Running on host `hostname --fqdn`");

x = float(sys.argv[1])
for i in range(0, 5):
    time.sleep(1)
    y = math.sqrt(x)
    print("x = "+str(y))
    x = y

print(datetime.datetime.now().strftime('Finished %Y %d %b %H:%M:%S\n'))
