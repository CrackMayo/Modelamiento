# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 12:10:43 2018

@author: carlos
"""
import matplotlib.pyplot as plt
import numpy as np

plt.xlim([-15,15])
plt.ylim([0,15])
xo = 10
vo = 0
g = 9.8
t = 0
k = 100
ka = 2
u = 0
m = 30
lo = 2
x = xo
v = vo
dt = 0.01
carro, = plt.plot(np.array([x,x+1,x+1,x,x]),np.array([1,1,2,2,1]))
llanta1, = plt.plot(x,1,'o')
llanta2, = plt.plot(x+1,1,'o')
resorte, = plt.plot(np.array([0,x]),np.array([1.5,1.5]))
ts = []
ys = []
while(t<40):
    t1 = t + dt
    v1 = ((k*(lo-x)-(ka*v))/m) * (t1-t) + v
    x1 = (v1)*(t1-t) + x
    x = x1
    t = t1
    v = v1        
    t = t + 0.1
    carro.set_xdata(np.array([x,x+1,x+1,x,x]))
    llanta1.set_xdata(x)
    llanta2.set_xdata(x+1)
    if(x<0):
        resorte.set_xdata(np.array([0,x+1]))
    else:
        resorte.set_xdata(np.array([0,x]))
    plt.pause(0.1)
    ts = np.concatenate((ts,np.array(x)),axis=None)
    ys = np.concatenate((ys,np.array(t)),axis=None)
    print("x = ",x)
plt.figure(2)
plt.plot(ys,ts,'b')    
plt.title("posicion vs tiempo")
plt.xlabel("tiempo")
plt.ylabel("posicion")
