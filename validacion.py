import os, platform
from multiprocessing import Process
from time import sleep
from datetime import datetime

PROCESS_WAIT_TIME = 10
SON_WAIT_TIME = 3
AMOUNT_PROCESSES = 10

def hijo():
    print("Iniciando el proceso: <", os.getpid(), "> a las <", datetime.now().strftime("%H:%M:%S"), ">")
    sleep(SON_WAIT_TIME)
    print("Terminando el proceso con pid <", os.getpid(), ">")
    os._exit(0)

def padreWindows():
    print("Pid Windows, padre: ", os.getpid())
    for i in range(AMOUNT_PROCESSES) :
        p = Process(target=hijo)
        p.start()
        p.join(0)
        sleep(PROCESS_WAIT_TIME)
        
def padreUnix():
    print("Pid padre: ", os.getpid())
    for i in range(AMOUNT_PROCESSES):
        sonPid = os.fork()
        if sonPid == 0:
            hijo()
        else: 
            sleep(PROCESS_WAIT_TIME)

if __name__ == '__main__' :
    if (platform.system() == "Windows"):
        padreWindows()
    else: 
        padreUnix()
