import matplotlib.pyplot as plt
import numpy as np
import math
plt.figure(figsize=(3,4))
x=np.arange(0,2*math.pi+0.005,.005)
y=np.sin(x)
plt.plot(x,y,"r--",label="sin")
plt.plot(x,np.cos(x),"go",label="cos")
plt.xlabel("angle")
plt.ylabel("sin cos tan")
plt.title("Trigonometry")
plt.grid(True)
plt.legend(loc="upper right")
plt.xticks(np.arange(0,2*math.pi+1,math.pi/4))
plt.yticks(np.arange(-1,1.1,.5))
plt.tick_params(axis="both",direction="in",rotation=40,colors="red")
plt.show()
