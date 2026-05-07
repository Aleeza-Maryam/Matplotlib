import matplotlib.pyplot as plt
import numpy as np

months=np.array(["Jan","Feb","March","April","May","June"])
rain=np.array([70,40,60,55,20,30])
plt.xlabel("Months")
plt.ylabel("Rain")
plt.title("Precipitation")

plt.plot(months,rain)
plt.show()