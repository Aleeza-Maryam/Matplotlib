import matplotlib.pyplot as plt
x=["p","q","r","s","t"]
y=[1,2,3,4,5]
c=["red","blue","yellow","orange","skyblue"]
# dots sizes
dots_size=[400,300,200,450,350]
plt.xlabel("day")
plt.ylabel("No")
plt.title("Basics of scatter plot")
# cmap (color map se bhi color change ho skte)
plt.scatter(x,y,label="Basics",color=c,sizes=dots_size,alpha=0.5,marker="v",cmap="viridis")  #or color="red"
t=plt.colorbar()       #aik range si show hoti
t.set_label("range palette")
plt.legend()
plt.show()


# multiple scatter plot
day=[15,4,3,7,8]
month=[4,7,12,9,14]
month2=[9,5,13,6,8]
colors=["red","orange","green","blue","yellow"]
plt.scatter(day,month,color=colors,label="multiple scatter plot",marker="s")
plt.scatter(day,month2,color=colors,marker="s")
plt.legend(loc="best")
plt.show()
