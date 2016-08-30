import socket
import random
from itertools import *
import signal,time
import re
from _socket import MSG_DONTWAIT
def sigUSR2_handler(signum,stacl):
    global MineA
    buf=sock.recv(30,MSG_DONTWAIT).decode("UTF-8")
    match=re.search(r"(?<=MineDim=)\S+?(?=\|)",buf)
    if match.group(0) is not None:
         matcher=re.search(r'\((\S+),(\S+)\)',match.group(0))
         Dim1=int(matcher.group(1))
         Dim2=int(matcher.group(2))
         MineDim=(Dim1,Dim2)
    match=re.search(r"(?<=MineNum=)\S+?(?=\|)",buf)
    if match.group(0) is not None:
         MineNum=int(match.group(0))
    MineA=Mine(MineDim,MineNum)
    for i in range(MineA.MineDim[0]):
        for j in range(MineA.MineDim[1]):
            sock.send(bytes(str(MineA.MineArray[i][j])+' ',"UTF-8"))
def sigUSR1_handler(signum,stack):
    global MineA
    for i in range(MineA.MineDim[0]):
        for j in range(MineA.MineDim[1]):
            sock.send(bytes(str(MineA.MineArray[i][j])+' ',"UTF-8"))
        #sock.send(bytes('\n',"UTF-8"))
class Mine(object):
    def __init__(self,MineDim,MineNum):
        self.MineDim=MineDim
        self.MineNum=MineNum
        MineList=[]
        self.genMineArray(MineDim,MineNum,MineList)
    def genMineArray(self,MineDim,MineNum,MineList):
        MineArray=[[0]*MineDim[0] for i in range(MineDim[1])]
        n=0
        while n<MineNum:
            i=random.randint(0,MineDim[0]-1)
            j=random.randint(0,MineDim[1]-1)
            if (i,j) not in MineList:
                MineList.append((i,j))
                n+=1
            
        print(len(MineList))
        for i,j in product(range(MineDim[0]),range(MineDim[1])):
            if (i,j) in MineList:
                MineArray[i][j]=1
            else:
                MineArray[i][j]=0
        self.MineArray=MineArray 
signal.signal(signal.SIGUSR1,sigUSR1_handler)
signal.signal(signal.SIGUSR2,sigUSR2_handler)

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost',5000))
if __name__=='__main__':
    MineA=Mine((10,10),10)
    while True:
        time.sleep(1)
    #signal pending
    
