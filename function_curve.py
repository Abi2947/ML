import numpy as np
import matplotlib.pyplot as plt

#Sin Function
start=np.linspace(-np.pi,np.pi,400)
end=np.sin(start)

fig=plt.figure(figsize=(5,5))


plt.plot(start,end,color='blue')
plt.title('Sin and Cos Function')
plt.xlabel("X")
plt.ylabel('Y')
plt.axhline(y=0)
plt.show

#Cos Function
start=np.linspace(-(2*np.pi),2*np.pi,400)
end=np.cos(start)


plt.plot(start,end,color='red')
plt.title('Sin and Cos Function')
plt.xlabel("X")
plt.ylabel('Y')
plt.axhline(y=0)
plt.show