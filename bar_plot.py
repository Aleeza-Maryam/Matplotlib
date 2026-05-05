import matplotlib.pyplot as plt    #from matplotlib import pyplot as plt

x=["python","c","c++","java","php"]
y=[90,60,80,82,78]
# labels 
plt.xlabel("languages",fontsize=15)
plt.ylabel("popularity",fontsize=15)
#  width of bars / colors
# plt.bar(x,y,width=0.5, color="r")
# multiple colors          
c=["r","y","m","g","b"]
# align parameter   (x labels ko edge pe krta...by default , center hota hai)
plt.bar(x,y,color=c,width=0.4,align="edge",edgecolor="black",linestyle="--",alpha=0.3,label="Comparison",position="center")                 #color="y"
plt.legend()
plt.show()


