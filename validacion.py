import os, platform
from multiprocessing import Process
from time import sleep
from datetime import datetime

if (platform.system() == "Windows"):
    def hijo():
        print("Iniciando el proceso: <", os.getpid(), "> a las <", datetime.now().strftime("%H:%M:%S"), ">")
        sleep(3)
        print("Terminando el proceso con pid <", os.getpid(), ">")
        os._exit(0)
    
    def padre():
        print("Pid Windows, padre: ", os.getpid())
        for i in range(10) :
            p = Process(target=hijo)
            p.start()
            sleep(10)
            p.join(0)
    
    if __name__ == '__main__' :
        padre()

elif (platform.system() == "Linux"):
    def padre():
        print("Pid padre: ", os.getpid())
        for i in range(10):
            sonPid = os.fork()
            sleep(10)
            if sonPid == 0:
                hijo()
          
    
    def hijo():
        print("Iniciando el proceso: <", os.getpid(), "> a las <", datetime.now().strftime("%H:%M:%S"), ">")
        sleep(3)
        print("Terminando el proceso con pid <", os.getpid(), ">")
        os._exit(0)
        
    if __name__ == '__main__' :
        padre()
