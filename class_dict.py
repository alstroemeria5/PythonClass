# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:50:24 2016

@author: root
"""
Verbose={'Shared':True}
import time,functools
import threading
from functools import *
def DecoDePrint(key):
    def DecoratedPrint(func):
        def Decorated(*args):
            global Verbose
            if key in Verbose:
                if Verbose[key] is True:
                    print(*args)
        return Decorated
    return DecoratedPrint
@DecoDePrint('Fuguzzi')
def StdPrint(*args):
    print(*args)
class CardDict(dict):
    def __init__(self,Version,*args,**kwargs):
        self.CardDictVersion=str(Version)
        print(Version)
        dict.__init__(self,*args,**kwargs)
        
    def __setitem__(self,key,value):
        if not isinstance(value,int):        
            if hasattr(value,'CardID'):
                value=value.CardID
                pass
            else:
                print("Value is neither a legitimate Card Object nor a Card Identifier")
                return None
        else:
            pass
        super(CardDict,self).__setitem__(key,value)
def DecoDeDrift(Role):
    def Decorator(func):
        if Role=='Server':
            def DecoratorServer(*args):
                Verbose=Role.Verb
                func(*args)
        return DecoratorServer
    return Decorator
@DecoDeDrift('Server')        
def AddressInterp(Packet):
    global Verbose
    if not (hasattr(Packet,subnet) and hasattr(Packetnet,subnetmask)):
            StdPrint("Either Packet has no subnet or packet has no subnetmask")
            return none 
            if  hasattr(DriftServer.ServerFingerPrint):
                DriftServer.FingerPrint(DriftServer,Packet.subnet,Packet.subnetmask)
                
            
        
        
class Average():
    def __init__(self):
        self.series=[]
    def __call__(self,new_value):
        self.series.append(new_value)
        total=sum(self.series)
        return total/len(self.series)
        
        
        
def make_averager():
    series=[]
    
    def averager(new_value):
        series.append(new_value)
        total=sum(series)
        return total/len(series)
        
    return averager
    
def make_2_averager():
    count=0
    total=0
    def averager(new_value):
        nonlocal count,total
        count+=1
        total+=new_value
        return total/count
    return averager
    

def clock(func):
    @functools.wraps(func)    
    def clocked(*args):
        nonlocal func
        t0=time.time()
        result=func(*args)
        elapsed=time.time()-t0
        name=func.__name__
        arg_str=', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s)->%r' %(elapsed,name,arg_str,result))
        return result
    return clocked
@wraps
def locked(func, *args, **kw):
    lock = getattr_(func, "lock", threading.Lock)
    lock.acquire()
    try:
        result = func(*args, **kw)
    finally:
        lock.release()
    return result
    
    
@clock
def snooze(seconds):
    time.sleep(seconds)
@clock
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)
"""@functools.lru_cache(maxsize=128)"""
@clock
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2)+fibonacci(n-1)
    

if __name__=='__main__':
    print('*'*40,'Calling snooze (.123)')
    snooze(.123)
    print('*'*40,'Calling factorial(6)')
    print('6!=',factorial(6))
    print(fibonacci(6))
