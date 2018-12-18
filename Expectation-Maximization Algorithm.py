#%%
import numpy as np
import pandas as pd
import copy
data=pd.read_csv('/home/joker/Desktop/5002/Data_Q4-20181207T172333Z-001/Q4_Data.csv')
data=np.array(data)



c1=[0,0,0,0,0,0]
c2=[1,1,1,1,1,1]
dict1={}
dict2={}

def distance(x,y):
    s=0
    for i in range(len(x)):
        s=s+(x[i]-y[i])**2
    return s

weight = np.zeros((len(data),2))
X1=[]
X2=[]

SSE=[]
w=[]
for k in range(0,100):
    sse=0
    for i in range(0,len(data)):
        weight[i][0]=distance(data[i],c2)/(distance(data[i],c2)+distance(data[i],c1))
        weight[i][1]=1-weight[i][0] 
        sse=sse+weight[i][0]*weight[i][0]*distance(data[i],c1)+weight[i][1]*weight[i][1]*distance(data[i],c2)

    SSE.append(sse)


    for j in range(0,6):
        c1s=0
        s1=0
        c2s=0
        s2=0
        for i in range(0,len(data)):
            c1s=c1s+data[i][j]*weight[i][0]**2
            s1=s1+weight[i][0]**2
            c2s=c2s+data[i][j]*weight[i][1]**2
            s2=s2+weight[i][1]**2
        c1[j]=c1s/s1
        c2[j]=c2s/s2

    dict1[k+1]=copy.deepcopy(c1)
    dict2[k+1]=copy.deepcopy(c2)
C1=list(dict1.values())
C2=list(dict2.values())  
    
d1=0
d2=0
for i in range(0,100):
    d1=sum([C1[i+1][j]-C1[i][j] for j in range(0,6)])
    d2=sum([C2[i+1][j]-C2[i][j] for j in range(0,6)])
    if (d1+d2<0.0001):
        print('iteration step:',i+1)
        print('final c1:',C1[i+1])
        print('final c2:',C2[i+1])
        break

print('the fisrt c1:',C1[0])
print('the fisrt c2:',C2[0])
print('the second c1:',C1[1])
print('the second c2:',C2[1])
#%%
c1=[0,0,0,0,0,0]
c2=[1,1,1,1,1,1]
weight1 = np.zeros((len(data),2))
weight2 = np.zeros((len(data),2))
for i in range(0,626):
    weight1[i][0]=distance(data[i],c2)/(distance(data[i],c2)+distance(data[i],c1))
    weight1[i][1]=1-weight1[i][0]
    weight2[i][0]=distance(data[i],C2[0])/(distance(data[i],C2[0])+distance(data[i],C1[0]))
    weight2[i][1]=1-weight1[i][1]


sse=0
sse1=0
for i in range(0,len(data)):
    sse=sse+weight1[i][0]*weight1[i][0]*distance(data[i],C1[0])+weight1[i][1]*weight1[i][1]*distance(data[i],C2[0])
    sse1=sse1+weight2[i][0]*weight2[i][0]*distance(data[i],C1[1])+weight2[i][1]*weight2[i][1]*distance(data[i],C2[1])


print('sse1:',sse)
print('sse2:',sse1)



