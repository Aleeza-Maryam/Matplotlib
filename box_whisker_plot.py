import matplotlib.pyplot as plt
x=[10,20,30,40,50,60,70]
plt.boxplot(x,notch=True)
plt.show()
plt.boxplot(x,vert=True,widths=0.2,label=['python'],patch_artist=True,showmeans=True)
plt.show()
x1=[10,20,30,40,50,60,70,120]   #outlier show ho ga
plt.boxplot(x1,sym="green",boxprops=dict(color="r"),capprops=dict(color="yellow"),whiskerprops=dict(color="red"),flierprops=dict(markeredgecolor="yellow"))    #whis=2 se join ho jae ga outlier
plt.show()


# multiple box plot
import matplotlib.pyplot as plt
x1=[10,20,30,40,50,60,70]
x2=[10,30,20,40,60,90,50]
y=[x1,x2]
plt.boxplot(y,labels=["python","c++"],showmeans=True,sym="green",boxprops=dict(color="green"),capprops=dict(color="yellow"))
plt.legend(loc="best")
plt.show()