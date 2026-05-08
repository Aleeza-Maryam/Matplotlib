import matplotlib.pyplot as plt
import numpy as np

x=np.random.randint(10,100,(40))
print(x)
l=[10,20,30,40,50,60]
plt.title("Histogram")
plt.xlabel("Python")
plt.ylabel("No.")
plt.hist(x,color="red",range=(10,50),edgecolor="black",bins="auto")
plt.show()
