import numpy as np
import matplotlib.pyplot as plt

y = 17.5
m = 0.1
g = 9.8
dt = 0.01
v = 0
r = 0.3
a = np.pi*(r**2)
t=0
k=0.98*0.8*a
plt.xlim(0,40)
plt.ylim(0,25)
masa,=plt.plot(20,y,'o')
paracaidas, = plt.plot(np.array([20,17,18,19,20,21,22,23,20,23,20,17]),np.array([y,y+1.5,y+2,y+2.25,y+2.4,y+2.25,y+2,y+1.5,y,y+1.5,y+1.5,y+1.5]))
edificio,=plt.plot(np.array([5,5,15,15,5,5,5,15,15,5,5,5,15,15,5,5,5,15,15,5,5,5,15,15,5,5,5,15,15]), np.array([0,3.5,3.5,0,0,3.5,7,7,3.5,3.5,7,10.5,10.5,7,7,10.5,14,14,10.5,10.5,14,17.5,17.5,14,14,17.5,21,21,17.5]),'k')
Vt = np.array([],float)
Vy = np.array([],float)
Vv = np.array([],float)
while y > 0.03:
    plt.pause(dt)
    vk=(-g+(k*v**2/m))*dt+v
    yk=v*dt+y
    y=yk
    v=vk
    paracaidas.set_ydata(np.array([y,y+1.5,y+2,y+2.25,y+2.4,y+2.25,y+2,y+1.5,y,y+1.5,y+1.5,y+1.5]))
    masa.set_ydata(yk)
    t=t+dt
    Vv= np.append(Vv,-vk)
    Vy= np.append(Vy,yk)
    Vt= np.append(Vt,t)  
    print("%1.2f"%t, yk) 
    
    
plt.figure("Tiempo vs Altura")  
plt.xlabel("Tiempo (s)", fontsize = 10)
plt.ylabel("Altura (m)", fontsize = 10)  
plt.plot(Vt,Vy,'b') 
plt.figure("Tiempo vs Velocidad")  
plt.xlabel("Tiempo (s)", fontsize = 10)
plt.ylabel("Velocidad (m/s)", fontsize = 10)
plt.plot(Vt,Vv,'b')