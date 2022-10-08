#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from asyncio import constants
import subprocess
  
def sendmessage(message="test"):
    subprocess.Popen(['notify-send', message])
    print('test')
    return
  
if __name__ == '__main__':
    sendmessage()