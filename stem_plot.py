import matplotlib.pyplot as plt
x=[4,3,5,2,6]
y=[5,3,2,4,1]
plt.stem(x,y,linefmt="r:",markerfmt="k*",bottom=2,basefmt="g",label="python")
plt.legend()
plt.show()



# boottom=2    By default lines 0 se shuru hoti hain, lekin yahan aapne 2 rakha hai, toh saari vertical lines y=2 se shuru hokar point tak jayengi.