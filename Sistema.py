import math as m

def function():
    L1=[]
    L2=[]
    L3=[]
    x1=0.1
    x2=1.0
    x3=10
    
    for i in range(5):
        L1.append(m.pow(x1,2)+1)
        L2.append(m.pow(x2,2)+1)
        L3.append(m.pow(x3,2)+1)
        x1=m.pow(x1,2)+1
        x2=m.pow(x2,2)+1
        x3=m.pow(x2,2)+1
    return L1,L2,L3

#print(function())

