import matplotlib.pyplot as plt
x=[4,3,5,2,6]
y=[5,3,2,4,1]
plt.stem(x,y,linefmt="r:",markerfmt="k*",bottom=2,basefmt="g",label="python")
plt.title("Stem plot")
plt.legend()
plt.show()



# bottom=2    By default lines 0 se shuru hoti hain, lekin yahan aapne 2 rakha hai, toh saari vertical lines y=2 se shuru hokar point tak jayengi.
# use_line_collection=False: Ye ek purana parameter hai jo performance ke liye use hota tha. Naye versions mein ise likhne ki zaroorat nahi padti, lekin yahan ye lines ko purane tarike se render karega
# Naye versions mein ye default True hota hai. Iska matlab hai ki Matplotlib saari vertical lines ko ek single "LineCollection" object mein pack kar deta hai.

# Matplotlib ko ab 100 alag objects nahi, sirf 1 "group" handle karna padta hai.

# Fayda: Ye bahut fast hai aur memory kam leta hai.