import matplotlib.pyplot as plt
x=[1,2,3,4,5]
area=[6,4,7,8,3]
plt.stackplot(x,area)
plt.show()


# multiple stack plots

area1=[5,4,7,2,6]
area2=[7,3,2,5,3]
area3=[6,4,8,3,1]
l=["area1","area2","area3"]
plt.stackplot(x,area1,area2,area3,colors=["red","skyblue","pink"],baseline="zero",labels=l)
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Stack plot / Area plot")
plt.show()