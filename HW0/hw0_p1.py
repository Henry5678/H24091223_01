# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:53:55 2021

@author: apple
"""
a=input("Input the polynomials:")
a1=a.lstrip("(")
a2=a1.rstrip(")")
c=a2.split(")(")

#print(c)
d=[]
d1=[]
d2=[]
for i in c:
    c1=i.split("+")
    d.append(c1)
for i in d:
    for j in i:
        if "-" in j:
            j=j.split("-")
            l=len(j)
            d1.append(j[0])
            for k in range(1,l):
                d1.append("-"+j[k])
        else:
            d1.append(j)
    d2.append(d1)
def mul(var1,var2):
    if "*" in var1:
        var1=var1.split("*")
        if "*" in var2:
            var2=var2.split("*")
            ans=int(var1[0])*int(var2[0])
            if var1[1]==var2[1]:
                e=str(int(ans))+"*"+str(var1[1])
            elif var1[1]!=var2[1]:
                e=str(int(ans))+"*"+str(var1[1])+str(var2[1])
        elif "*" not in var2:
            if var2.isdigit():
                e=str(int(var1[0])*int(var2))+"*"+str(int(var1[1]))
            else:
                e=str(int(var1[0]))+"*"+str(var1[1])+str(var2)
    elif "*" not in var1:
        if "*" in var2:
            var2=var2.split("*")
            if var1.isdigit():
                ans=int(var1)*int(var2[0])
                e=str(ans)+"*"+str(var2[1])
            else:
                e=str(int(var2[0]))+"*"+str(var1)+str(var2[1])
        elif "*" not in var2:
            if var1.isdigit():
                if var2.isdigit():
                    e=str(int(var1)*int(var2))
                else:
                    e=str(int(var1)+"*"+str(var2) 
            else:
                if var2.isdigit():
                    e=str(int(var2))+"*"+str(var1)
                else:
                    e=str(int(var1)+str(var2)
    return e
#取分項帶入mul
elm=[]
ans=[]
for i in d2:
    for j in i:
        for k in ans:
            elm.append(mul(j,k))
    ans=elm       
print(ans)

#變數
f=[]
for i in ans:
    if "*" in i:
        i=i.split("*")
        f.append(i[1])

        





           