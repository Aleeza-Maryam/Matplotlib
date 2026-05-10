import matplotlib.pyplot as plt
x=[10,20,30,40]
ex=[0.0,0.0,0.0,0.2]
c=["red","green","blue","yellow"]
y=["C","C++","Java","Python"]
plt.pie(x,labels=y,explode=ex,colors=c,autopct="%0.1f%%",shadow=True,radius=1.3,labeldistance=1.1,startangle=180,textprops={"fontsize":10},counterclock=False,wedgeprops={"edgecolor":"m"},center=(3,3),rotatelabels=False)
plt.legend(loc=1)
plt.show()
plt.pie([1])
plt.show()


x1=[10,20,30,40]
c=["red","green","blue","yellow"]
y1=["C","C++","Java","Python"]
x2=[10,70,40,90]
plt.pie(x1,labels=y1,radius=1.0)
plt.pie(x2,radius=0.5,colors=c)
plt.show()



x2=[10,20,30,40]
c=["red","green","blue","yellow"]
y1=["C","C++","Java","Python"]
x3=[10,70,40,90]
plt.pie(x2,labels=y1,radius=1.5)
cr=plt.Circle(xy=(0,0),radius=1,facecolor="w")
plt.gca().add_artist(cr)
plt.show()

# plt.gca() ka matlab hai "Get Current Axes".

# add_artist(cr) us circle ko pie chart ke upar chipka deta hai, jis se wo beech se khali (donut jaisa) lagne lagta hai.