#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 13:36:01 2019

@author: ujjwal
"""

import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
import math

data = pd.read_csv('/home/ujjwal/Programing/6th_SEM/Data_Mining/iris.csv').values

x=data[:,:-1]
y=data[:,-1]

k=3

m=np.shape(x)[0]
n=np.shape(x)[1]

def norm(a):
    row=np.shape(a)[0]
    minpos = np.argmin(a)
    maxpos = np.argmax(a)
    old_max=a[maxpos]
    old_min=a[minpos]
    new_min=0
    new_max=1
    
    coff=(new_max-new_min)/(old_max-old_min)
    
    for i in range(row):
        v=(coff*(a[i]-old_min))+new_min
        a[i]=v
            
    return

for i in range(n):
    norm(x[:,i])
    
a=np.zeros((m,m))
for i in range (m):
    for j in range (m):
        a[i][j]=euclidean([x[i,:]],[x[j,:]])

c=[]
for i in range(m):
    avg=np.average(a[i])
    temp=set()
    for j in range(m): 
        if(a[i][j]<avg):
            temp.add(j)  
    c.append(temp)
    
temp=[]
for i in range(m):
    for j in range(i,m):
        if(c[i].issubset(c[j]) and i !=j):
            temp.append(i)
            break;

print((temp))

C=c.copy()
for i in range(len(temp)):
    C.remove(c[temp[i]])
    
def simlarity(temp1,temp2):
    intersect=temp1.intersection(temp2)
    union=temp1.union(temp2)
    
    return len(intersect)/len(union)

def find_sm(a):
    m=np.shape(a)[0]
    n=np.shape(a)[1]
    max=0
    for i in range(m):
        for j in range(n):
            if(a[i][j]>max and a[i][j]!=1):
                max=a[i][j]
                ptr1,ptr2=i,j
    
    return ptr1,ptr2

size=len(C)
c=C.copy()
#print(size)
while size > k :
    a=np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            a[i][j]=simlarity(c[i],c[j])
    
    x_i,y_i = find_sm(a)
    
    c[x_i]=(c[x_i].union(c[y_i])).copy()
    c.remove(c[y_i])
    size=len(c)
    
    temp=[]
    for i in range(size):
        for j in range(i+1,size):
            if(c[i].issubset(c[j])):
                temp.append(i)
                break;
    
    C=c.copy()
    for i in range(len(temp)):
        C.remove(c[temp[i]])
    
    size=len(C)
    c=C.copy()
    print(size)

points=[]
for i in range(size):
    points.append(list(C[i]))

colors=["red","blue","yellow"]    
for i in range(size):
    for j in range(len(points[i])):
        plt.scatter(x[points[i][j]][0]+x[points[i][j]][1],x[points[i][j]][2]+x[points[i][j]][3],s = 50, c = colors[i], marker='*')

d=[]
centroid=[]
for i in range(len(points)):
    for j in range(len(points[i])):
        dist=0
        for k in range(4):
            dist = dist + np.square(x[points[i][j]][k])
        d.append(np.sqrt(dist))
            
    d.sort()
    sz=len(d)
    print(sz)
    if(sz%2!=0):
        centroid.append(d[math.ceil(sz/2)])
    else:
        centroid.append((d[math.ceil(sz/2)]+d[int(sz/2)])/2)
    

    
