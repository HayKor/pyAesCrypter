import os
import pyAesCrypt as pas
from colorama import Fore
import sys

def menu():
    os.system("clear")
    print("")
    print("Автор: TG @HayKor          VK @barusidoo")
    print("")
    c = ''' d88b                   w              
8P    8d8b Yb  dP 88b. w8ww .d88b 8d8b 
8b    8P    YbdP  8  8  8   8.dP' 8P   
`Y88P 8      dP   88P'  Y8P `Y88P 8    
            dP    8                    '''
    print(c)
    print("")
    print("")
    print("")
    print("[1] Зашифровать")
    print("[2] Расшифровать")
    print("")
    choose = input("[*]Выберите вариант: ")
    if choose == "1":
           print("")
           print("[1] Зашифровать папку")
           print("[2] Зашифровать файл")
           choosedirfile = input("[*]Выберите вариант: ")
           if choosedirfile == "1":
                dir = input("Введите путь к папке ( с '/' ): ")
                parsdir(dir)
                crypt(dir)                  
           elif choosedirfile == "2":
                dir = input("Введите путь к файлу: ")
                crypterFile(dir)
    elif choose == "2":
         print("")
         print("[1] Расшифровать папку")
         print("[2] Расшифровать файл")
         choosedirfile = input("[*]Выберите вариант: ")
         if choosedirfile == "1":
             dir = input("Введите путь к папке ( с '/' ): ")
             parsdir(dir)
             decrypt(dir)
         elif choosedirfile == "2":
             dir = input("Введите путь к файлу: ")
             decrypterFile(dir)
         
		    

def decrypterFile(dir):
        password = input("Введите пароль: ")
        buffersize = 512*1024
        dirnoaes = os.path.splitext(dir)[0]
        pas.decryptFile(dir, dirnoaes, password, buffersize)
        print(Fore.GREEN + dir + " расшифровано!")
        os.remove(dir)
        
def crypterFile(dir):
        password = input("Введите пароль: ")
        buffersize = 512*1024
        pas.encryptFile(dir, dir + '.aes', password, buffersize)
        print(Fore.GREEN + dir + " зашифровано!")
        os.remove(dir)
        


def decrypt(dir):
        password = input("Введите пароль: ")
        buffersize = 512*1024
        for name in os.listdir(dir):
            if os.path.isfile(os.path.join(dir,name)):
                dirname = os.path.join(dir, name)
                dirnames = os.path.splitext(dirname)[0]
              #  result = ""
              #  dirnames = dirname.split(".aes")
               # for i in dirnames:
                    #dirnames = result + i
            pas.decryptFile(dirname,dirnames,password,buffersize)
            os.remove(dirname)
            print(Fore.GREEN + '[+] ' + dirname + ' расшифровано!')
		 
		 
def crypt(dir):
         password = input('Введите пароль: ')
         bufferSize = 512*1024 
         for name in os.listdir(dir):
         	if  os.path.isfile(os.path.join(dir,name)):
                       dirname = os.path.join(dir, name)
                       pas.encryptFile(dirname, dirname +'.aes', password, bufferSize) 
                       os.remove(dirname)
                       print(Fore.GREEN + '[+] '+ dirname +'.aes' + ' зашифровано!')

def parsdir(dir):
         for name in os.listdir(dir):
                 if  os.path.isfile(os.path.join(dir,name)):
                         print ('Файл: '+os.path.join(dir,name))
                 else :
                         if os.path.isdir(os.path.join(dir,name)) :
                                 parsdir(os.path.join(dir,name))
                                 
menu()
