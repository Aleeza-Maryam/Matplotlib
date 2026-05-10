import matplotlib.pyplot as plt
x=[10,20,30,40]
ex=[0.0,0.0,0.0,0.2]
c=["red","green","blue","yellow"]
y=["C","C++","Java","Python"]
plt.pie(x,labels=y,explode=ex,colors=c,autopct="%0.1f%%",shadow=True,radius=1.3,labeldistance=1.1,startangle=180,textprops={"fontsize":10},counterclock=False)
plt.show()