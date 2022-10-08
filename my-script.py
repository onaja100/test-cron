#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from asyncio import constants
import subprocess
  
def sendmessage(message="test"):
    subprocess.Popen(['notify-send', message])
    print('from github')
    print('test2')
    return
  
if __name__ == '__main__':
    sendmessage()
