import statistics
import math

from numpy import append

def norm(x,mean, stdev):  return (1/(stdev*(math.sqrt(2*math.pi)))) * (math.e**(-0.5*(((x - mean)/stdev)**2)))
def mx(outcomes): 
    mx=0
    rmx=""
    for i in outcomes: 
        if outcomes[i]>mx:
            mx=outcomes[i]
            rmx=i
    return rmx

def outcol(dat):
    cols={}
    for i in dat:
        d=i.split(",")
        for j in d:
            j=j.split("\n")
        for j in range(len(d)):
            if j not in cols:cols[j]=[d[j]]
            else: cols[j].append(d[j])
    min=-1
    rmin=0
    for i in cols:
        t={}
        for j in cols[i]:
            if j not in t : t[j]=1
        if min==-1:
            min=len(t.keys())
            rmin=i+1
        else:
            if len(t.keys())<min: 
                min=len(t.keys())       
                rmin=i+1
    return rmin 
            

path=r"C:\Users\ASUS\OneDrive\Desktop\winequality-red.csv"
dat=open(path)
oci=12 #output quality column
c=0
data=[]
outcomes={}
orout=[]
coln=0
for i in dat:
    coln=len(i.split(","))
    if c!=0:
        d=[]
        for j in range(coln): 
            if j!=oci-1: d.append(float(i.split(",")[j])) 
        ocm=i.split(",")[oci-1].split("\n")[0]
        if  ocm not in outcomes: 
            outcomes[ocm]=[1,[d],[],[]]
        else: 
            outcomes[ocm][0]+=1
            outcomes[ocm][1].append(d)
        orout.append(str(ocm))
    c+=1
for j in outcomes: 
    outcomes[j][0]/=(c-1)
    for k in range(coln-1):
        tempdat=[]
        for i in range(len(outcomes[j][1])):
            tempdat.append(outcomes[j][1][i][k])
        outcomes[j][2].append(statistics.mean(tempdat))
        outcomes[j][3].append(statistics.pstdev(tempdat))
dat=open(path)
c=0
out=0
for i in dat:
    if c!=0:
        t={}
        for j in outcomes: t[j]=outcomes[j][0]
        for j in range(coln):
            if j!=oci-1:
                num=float(i.split(",")[j].split("\n")[0])
                for k in outcomes:
                    if j>oci-1:t[k]*=norm(num,outcomes[k][2][j-1],outcomes[k][3][j-1])
                    else: t[k]*=norm(num,outcomes[k][2][j],outcomes[k][3][j])
        if str(mx(t))==str(i.split(",")[oci-1].split("\n")[0]): out+=1
    c+=1
print(100*(out/(c-1)))     

# how to connect to github