import os, platform
from multiprocessing import Process
from time import sleep
from datetime import datetime

PROCESS_WAIT_TIME = 10
SON_WAIT_TIME = 3
AMOUNT_PROCESSES = 10
if (platform.system() == "Windows"):
    def hijo():
        print("Iniciando el proceso: <", os.getpid(), "> a las <", datetime.now().strftime("%H:%M:%S"), ">")
        sleep(SON_WAIT_TIME)
        print("Terminando el proceso con pid <", os.getpid(), ">")
        os._exit(0)
    
    def padre():
        print("Pid Windows, padre: ", os.getpid())
        for i in range(AMOUNT_PROCESSES) :
            p = Process(target=hijo)
            p.start()
            sleep(PROCESS_WAIT_TIME)
            p.join(0)
    
    if __name__ == '__main__' :
        padre()

elif (platform.system() == "Linux"):
    def padre():
        print("Pid padre: ", os.getpid())
        for i in range(AMOUNT_PROCESSES):
            sonPid = os.fork()
            sleep(PROCESS_WAIT_TIME)
            if sonPid == 0:
                hijo()
          
    
    def hijo():
        print("Iniciando el proceso: <", os.getpid(), "> a las <", datetime.now().strftime("%H:%M:%S"), ">")
        sleep(SON_WAIT_TIME)
        print("Terminando el proceso con pid <", os.getpid(), ">")
        os._exit(0)
        
    if __name__ == '__main__' :
        padre()
