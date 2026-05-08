import matplotlib.pyplot as plt
import numpy as np

x=np.random.randint(10,100,(40))
print(x)
l=[10,20,30,40,50,60]
plt.title("Histogram")
plt.xlabel("Python")
plt.ylabel("No.")
plt.hist(x,color="red",range=(10,50),edgecolor="black",bins="auto",cumulative=-1,bottom=5,histtype="stepfilled",orientation="vertical",rwidth=0.7,log=True,label="python")
plt.axvline(20,color="green",label="Partition")
plt.grid()
plt.legend()
plt.show()
# Maslan, agar 10 se 20 ke darmiyan 5 random numbers aaye hain, toh us bar (bin) ki height y-axis par 5 tak jaye gi




# Bins data ko range mein divide karte hain. Maslan:

# Bin 1: 0-10 saal tak ke log.

# Bin 2: 11-20 saal tak ke log.

# Bin 3: 21-30 saal tak ke log.