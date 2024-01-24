import matplotlib.pyplot as plt  #install library - creating a virtual enviroment and installing into that enviroment 
import numpy as np               #step 1 create virtual enviroment in terminal window py - 3 -m venv myvenv
                                # activate your virtual enviroment 
x = np.linspace(0, 20, 100)       #install third party module
plt.plot(x, np.sin(x))

plt.show()

print("Hello World")
