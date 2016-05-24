#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import traceback
import os
import sys
import importlib
from config import config
from core import *

if __name__ == "__main__":
    try:  
        speech_manager = SpeechManager()
        speech_manager.welcome()
        # Init modules :
        if len(config.ENABLED_MODULES) > 0:
            module_manager = ModulesManager()
            for module_name in config.ENABLED_MODULES:
                pkg_name = ''.join(x for x in module_name.title().replace('_', '') if not x.isspace())
                module = importlib.import_module("modules."+pkg_name+"."+module_name)
                class_ = getattr(module, pkg_name)                
                instance = class_()
                module_manager.register_module(instance)
            # Start listening :
            isModule = False
            while True:
                keyword = speech_manager.speech_to_text()
                if keyword != "" :
                    print("\n\rKeyword : "+keyword)
                    isModule = module_manager.load_module(keyword)
                if isModule == False or keyword == "":
                    print("\n\rNo module found")
                    speech_manager.fail()
        else:
            raise Exception('All the modules are disabled')
    except Exception as e:
        traceback.print_exc()
        print(e.__str__())