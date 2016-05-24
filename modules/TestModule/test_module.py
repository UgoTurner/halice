#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import sys
from modules import base_module
from core import speech_manager
from datetime import datetime
from urllib.request import urlopen
import requests

class TestModule(base_module.BaseModule): 

    def __init__(self):        
        base_module.BaseModule.__init__(self, "test", speech_manager.SpeechManager())

    def do(self, keyword):
        if keyword == "say hello":
            self.speech_manager.say("Hello world !")
        elif keyword == "time":
        	current_time = datetime.strftime(datetime.now(), '%H:%M')
        	self.speech_manager.say("It is "+current_time)
        elif keyword == "who are you":
        	self.speech_manager.say("My name is Halice")
        elif "web" in keyword.lower():
            os.popen('chromium-browser &')
        elif keyword == "exit":
        	self.speech_manager.say("Closing "+self.name+" module")
        	self.is_active = False
        else:
            return False
        return True