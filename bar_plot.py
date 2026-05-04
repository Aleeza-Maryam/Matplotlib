import matplotlib.pyplot as plt    #from matplotlib import pyplot as plt

x=["python","c","c++","java","php"]
y=[90,60,80,82,78]
# labels 
plt.xlabel("languages",fontsize=15)
plt.ylabel("popularity",fontsize=15)
#  width of bars / colors
plt.bar(x,y,width=0.5, color="r")
# multiple colors
c=["r","y","m","g","b"]
plt.bar(x,y,color=c,width=0.4)
plt.show()

