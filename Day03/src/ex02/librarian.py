#!/usr/bin/env python3
import os

def install():
    try:
        if os.environ['VIRTUAL_ENV'][-8:] == "lauriefl":
            os.system("pip install Beautifulsoup4 pytest")
            os.system("pip freeze")
            os.system("pip freeze > requirements.txt")
    except:
        print("Неверное окружение")

if __name__ == '__main__':
    install()