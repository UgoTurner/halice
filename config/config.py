import os

LANG = "en"
ROOT_DIR =  os.getcwd()
CORE_DIR = ROOT_DIR+"/core"
SH_DIR = CORE_DIR+"/sh/"
SOUNDS_DIR = CORE_DIR+"/sounds/"
LOGS_DIR = CORE_DIR+"/logs/"
LOGS_FILE = LOGS_DIR+"/logs.txt"
ENABLED_MODULES = ["test_module"] # add new module to the list here