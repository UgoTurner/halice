#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

from gtts import gTTS
import os
import sys
from config import config
import json
import subprocess

class SpeechManager(object):

    def say(self, str):
        print("Say '"+str+"'")
        tts = gTTS(text=str, lang=config.LANG)
        tts.save(config.SH_DIR+"out.mp3")
        os.system("mpg321 -q "+config.SH_DIR+"out.mp3")

    def speech_to_text(self):
        keyword = ""
        #os.popen('sh '+config.SH_DIR+'speech_to_text.sh')
        p = subprocess.Popen(["sh", config.SH_DIR+'speech_to_text.sh'])
        p.communicate()
        with open(config.SH_DIR+'result.json') as f:
            res  = [x.strip('\n') for x in f.readlines()]
        if(len(res) == 2):
            data = json.loads(res[1])
            keyword = data['result'][0]['alternative'][0]['transcript']
        return keyword

    def welcome(self):
        os.system('mpg321 -q '+config.SOUNDS_DIR+'welcome.mp3')
        return

    def listen(self):
        os.system('mpg321 -q '+config.SOUNDS_DIR+'listening.mp3')
        return

    def fail(self):
        os.system('mpg321 -q '+config.SOUNDS_DIR+'nothing.mp3')
        return