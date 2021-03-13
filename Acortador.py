import time
import urllib.request
RED = '\033[31m'
WHITE = '\033[37m'

while True:
    print(RED+"""
 _____             _         _             _____ 
|  _  |___ ___ ___| |_ ___ _| |___ ___ ___| __  |
|     |  _| . |  _|  _| .'| . | . |  _|___| __ -|
|__|__|___|___|_| |_| |__,|___|___|_|     |_____|""")
    print(WHITE+"-Programado por:", RED+"Balta")

    def tiny_url(url):
        apiurl = "http://tinyurl.com/api-create.php?url="
        tinyurl = urllib.request.urlopen(apiurl+url).read()
        return tinyurl.decode("utf-8")

    url = input("ingrese aqui su direccion url a acortar: ")
    print(tiny_url(url))
