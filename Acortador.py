import time
import pyshorteners
RED = '\033[31m'
WHITE = '\033[37m'

while True:
    print(RED+"""
 _____             _         _             _____ 
|  _  |___ ___ ___| |_ ___ _| |___ ___ ___| __  |
|     |  _| . |  _|  _| .'| . | . |  _|___| __ -|
|__|__|___|___|_| |_| |__,|___|___|_|     |_____|""")
    print(WHITE+"-Programado por:", RED+"Balta")

    link = input(WHITE+"\n-> Link para Acortar: ")

    print("\nLink Acortado: " + str(pyshorteners.Shortener().tinyurl.short(link)))
    time.sleep(3)
