import matplotlib.pyplot as plt    #from matplotlib import pyplot as plt

x=["python","c","c++","java","php"]
y=[90,60,80,82,78]
z=[20,30,50,60,70]
# labels 
plt.xlabel("languages",fontsize=15)
plt.ylabel("popularity",fontsize=15)
#  width of bars / colors
# plt.bar(x,y,width=0.5, color="r")
# multiple colors          
c=["r","y","m","g","b"]
# align parameter   (x labels ko edge pe krta...by default , center hota hai)

# -----------------------overlapping ho gi isse-----------------------#
plt.bar(x,y,color="red",width=0.4,align="edge",edgecolor="black",linestyle="-",label="Comparison")
plt.bar(x,z,color="yellow",width=0.4,align="edge",edgecolor="black",linestyle="-",label="Comparison1")                  #color="y"
plt.legend()
plt.show()






# -----------------------isse bhi overlapping hogi-------------------------#
import numpy as np
x1=["python","c","c++","java","php"]
y1=[90,60,80,82,78]
z1=[20,30,50,60,70]
p=np.arange(len(x1))

# labels 
plt.xlabel("languages2",fontsize=15)
plt.ylabel("No",fontsize=15)
width=0.2

plt.bar(p,y1,color="red",align="edge",edgecolor="black",linestyle="-",label="Comparison")
plt.bar(p,z1,color="yellow",align="edge",edgecolor="black",linestyle="-",label="Comparison1")                  #color="y"
plt.legend()
plt.show()




# ----------------------isse overlapping ni hogi-------------------------#

x2=["python","c","c++","java","php"]
y2=[90,60,80,82,78]
z2=[20,30,50,60,70]
width2=0.3
p1=np.arange(len(x2))
p2=[j+width2 for j in p1]
# labels 
plt.xlabel("languages2",fontsize=15)
plt.ylabel("No",fontsize=15)


plt.bar(p1,y2,width2,color="red",align="edge",edgecolor="black",linestyle="-",label="Comparison")
plt.bar(p2,z2,width2,color="yellow",align="edge",edgecolor="black",linestyle="-",label="Comparison1")   
plt.xticks(p1 + width2/2, x2,rotation=20)        
plt.legend(loc="best")
plt.title("Grouped bar chart")
plt.show()

# Code 2 vs Code 3 (The Shifting)
# Code 2 mein: Humne p (yani 0, 1, 2...) ko sirf isliye use kiya taakay hum strings ki jagah numbers par bars bana sakein. Lekin humne shifting nahi ki, bas un numbers ko as a base use kiya.

# Code 3 mein: Humne numpy ka asli faida uthaya. Humne p1 (0, 1, 2...) liya aur phir us mein width jama (add) kar di taakay dusre bar ke liye coordinates badal jayein.




#-------------------------horizontal bar graph---------------------#

x3=["python","c","c++","java","php"]
y3=[90,60,80,82,78]
z3=[20,30,50,60,70]
height_val=0.3
p3=np.arange(len(x3))
p4=[j+height_val for j in p3]
# labels 
plt.ylabel("languages2",fontsize=15)
plt.xlabel("popularity",fontsize=15)


plt.barh(p3,y3,height_val,color="red",edgecolor="black",linestyle="-",label="Comparison")
plt.barh(p4,z3,height_val,color="yellow",edgecolor="black",linestyle="-",label="Comparison1")   
plt.yticks(p3 + height_val/2, x3,rotation=20)        
plt.legend(loc="best")
plt.title("Grouped bar chart")
plt.show()


