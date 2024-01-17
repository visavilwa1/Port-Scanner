#!/bin/python3
import sys
import socket 
from datetime import datetime

#Define Our target
if len (sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPV4
else: 
	print ("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
