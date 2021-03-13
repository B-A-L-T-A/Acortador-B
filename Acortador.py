import time
import urllib.request
from colorama import init, Fore

while True:
    print(Fore.YELLOW + """
 _____             _         _             _____ 
|  _  |___ ___ ___| |_ ___ _| |___ ___ ___| __  |
|     |  _| . |  _|  _| .'| . | . |  _|___| __ -|
|__|__|___|___|_| |_| |__,|___|___|_|     |_____|""")
    print(Fore.YELLOW + "C", end="")
    print(Fore.GREEN + "o", end="")
    print(Fore.BLUE + "d", end="")
    print(Fore.RED + "e", end="")
    print(Fore.CYAN + "d ", end="")
    print(Fore.MAGENTA + "b", end="")
    print(Fore.WHITE + "y ", end="")
    print(Fore.YELLOW + "B", end="")
    print(Fore.RED + "a", end="")
    print(Fore.YELLOW + "l", end="")
    print(Fore.GREEN + "t", end="")
    print(Fore.BLUE + "a", end="")
    print(Fore.YELLOW +"\n")

    def tiny_url(url):
        apiurl = "http://tinyurl.com/api-create.php?url="
        tinyurl = urllib.request.urlopen(apiurl+url).read()
        return tinyurl.decode("utf-8")

    url = input(">>> ingrese aqui su direccion url a acortar: ")
    print(">>> Url acortado: ", tiny_url(url))
    time.sleep(3)

