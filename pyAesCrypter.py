import os
import pyAesCrypt as pas

def menu():
        print("Автор: TG @HayKor")
        print("")
        c = ''' a88888b.                              dP                     
d8'   `88                              88                     
88        88d888b. dP    dP 88d888b. d8888P .d8888b. 88d888b. 
88        88'  `88 88    88 88'  `88   88   88ooood8 88'  `88 
Y8.   .88 88       88.  .88 88.  .88   88   88.  ... 88       
 Y88888P' dP       `8888P88 88Y888P'   dP   `88888P' dP       
                        .88 88                                
                    d8888P  dP                                '''
        print(c)
        print("")
        print("")
        print("")
        print("[1] Зашифровать")
        print("[2] Расшифровать")
        print("")
        choose = input("[*]Выберите вариант: ")
        if choose == "1":
                dir = input("Введите путь к файлу/папке: ")
                parsdir(dir)
                crypt(dir)	
        elif choose == "2":
                dir = input("Введите путь к файлу без .aes: ")
                parsdir(dir)
                decrypt(dir)
		    


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
            print('[+] ' + dirname + ' расшифровано!')
		 
		 
def crypt(dir):
         password = input('Введите пароль: ')
         bufferSize = 512*1024 
         for name in os.listdir(dir):
         	if  os.path.isfile(os.path.join(dir,name)):
                       dirname = os.path.join(dir, name)
                       pas.encryptFile(dirname, dirname +'.aes', password, bufferSize) 
                       os.remove(dirname)
                       print('[+] '+ dirname +'.aes' + ' зашифровано!')

def parsdir(dir):
         for name in os.listdir(dir):
                 if  os.path.isfile(os.path.join(dir,name)):
                         print ('Файл: '+os.path.join(dir,name))
                 else :
                         if os.path.isdir(os.path.join(dir,name)) :
                                 parsdir(os.path.join(dir,name))
                                 
menu()