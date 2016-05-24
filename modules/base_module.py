#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

class BaseModule:
    
    def __init__(self, module_name, speech_manager):        
        self.is_active = False
        self.name = module_name
        self.speech_manager = speech_manager
    
    def load(self):
        print("\n\rModule "+self.name+" started\n\r")
        self.speech_manager.say("Module : "+self.name)
        self.is_active = True
        understood = False
        while self.is_active == True:
            keyword = self.speech_manager.speech_to_text()
            print("\n\rKeyword : "+keyword)
            if keyword != "":
                understood = self.do(keyword)
            if understood == False:
                print("\n\rNo action found")
                self.speech_manager.fail()