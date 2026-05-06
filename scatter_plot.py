import matplotlib.pyplot as plt
x=["p","q","r","s","t"]
y=[1,2,3,4,5]
c=["red","blue","yellow","orange","skyblue"]
plt.xlabel("day")
plt.ylabel("No")
plt.title("Basics of scatter plot")
plt.scatter(x,y,label="Basics",color=c)
plt.legend()
plt.show()
