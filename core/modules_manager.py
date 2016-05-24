#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import os
import time
import json
import sys
from config import config
from modules import *

class ModulesManager(object): 

    def __init__(self):
        self.modules = {}

    def register_module(self, module):
        print("Register module "+module.name+"\r\n")
        self.modules[module.name] = module
        
    def load_module(self, module_name):
        if module_name in self.modules.keys():
            print("Load module "+module_name+"\r\n")
            self.modules[module_name].load()
        else:
            return False    