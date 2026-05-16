import matplotlib.pyplot as plt
x=[10,20,30,40,50,60,70]
plt.boxplot(x,notch=True)
plt.show()
plt.boxplot(x,vert=True,widths=0.2,label=['python'],patch_artist=True,showmeans=True)
plt.show()
x1=[10,20,30,40,50,60,70,120]
plt.boxplot(x1)
plt.show()