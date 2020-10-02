# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:15:10 2020

@author: ANJALI
"""

def australian_tennis(d):
    totalscore=dict()
    for i in d:
        for j in d[i]:
            if j in totalscore:
                totalscore[j]+=d[i][j]
            else:
                totalscore[j]=d[i][j]
    best=max(totalscore,key=totalscore.get)
    return best,totalscore[best]
games={'test1':{'Samantha Stour':7,'Astra Sharma':8},
       'test2':{'Astra Sharma':5,'Ellen Perez':9}}
print(australian_tennis(games))
