# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 10:29:34 2021

@author: apple
"""


filename="IMDB-Movie-Data.csv"
f=open(filename,'r',encoding="utf-8")
movie=f.read()
mov=movie.split("\n")
#f.close()
mov=mov[0:len(mov)-1]
for i in range(len(mov)):
	mov[i]=str(mov[i]).split(",")    
a=int(input("I want the answer of question No.\n(1) Top-3 movies with the highest ratings in 2016?\n(2) The actor generating the highest average revenue?\n(3) The average rating of Emma Watson’s movies?\n(4) Top-3 directors who collaborate with the most actors?\n(5) Top-2 actors playing in the most genres of movies?\n(6)Top-3 actors whose movies lead to the largest maximum gap of years?\n(7)Find all actors who collaborate with Johnny Depp in direct and indirect ways: ")) 
#[1]
if a==1:
    x=[]
    y=[]
    z={}
    for i in range(len(mov)):
        b=mov[i][5]
        c=mov[i][7]
        d=mov[i][1]
        if b =="2016":
            x.append(d)
            y.append(c)
            y1 = list(map(float,y))
            z=dict(zip(x,y1))
            sorted(z.items(),key = lambda x:x[1],reverse=True)
    print("1st:%s\n2nd:%s\n3rd:%s"%(list(z.keys())[0],list(z.keys())[1],list(z.keys())[2]))
#    print(z) 
#[2]      
elif a==2:
    x=[]
    y=[]
    for i in range(1,len(mov)):
        b=mov[i][4]
        b1=b.split("|")
        for j in b1:
            if j.lstrip() not in x:
                x.append(j.lstrip()) 
    z={}            
    for i in x:
        z[i]=[0,0]
    for i in range(1,len(mov)):
        c=mov[i][9]
        if c!="":
           b=mov[i][4] 
           b1=b.split("|") 
           for j in b1:
               y.append(j.lstrip())
           for j in y:
               d=z[j]
               d[0]=d[0]+float(c)
               d[1]=d[1]+1
               z[j]=d
        y=[] 
    e=0
    for j in x:
        d=z[j]
        if d[1]!=0:
            f=d[0]/d[1]
        if f>e:
            e=f
            g=j

#並列
    w1=[]       
    for j in x:
        if d[1]!=0:
           f=d[0]/d[1]
        if f==e and j!=g:
            w1.append(j)
    print("The actor generating the highest average revenue:%s"%(g))        
    if w1!=[]:
        print("並列:",w1)
#[3]        
elif a==3:
    rating=[0,0] #[總和,個數]
    x=[]
    y=0
    for i in range(1,len(mov)):
        if "Emma Watson" in mov[i][4]:
            x.append(mov[i][7])
            num=len(x)
            x1 = list(map(float,x))
            sum1=sum(x1)
            avg1=sum1/num       
    print("The average rating of Emma Watson’s movies:",avg1)
#[4]        
elif a==4:
    x=[]#actor
    y=[]#director
    z={}#[director,actor]          
    for i in range(1,len(mov)):
        c=mov[i][3]
        y.append(c)
        y1=list(set(y))
        originy=sorted(y1,key=y.index)
    for i in originy:
        z[i]=set()
    for i in range(1,len(mov)):
        c=mov[i][3]
        d=z[c]
        b=mov[i][4]
        b1=b.split("|")
        for j in b1:
            x.append(j.lstrip())
        d=set(d) | set(x)
        z[c]=d
    z1=[0,0]#[name,total]
    z2=[0,0]
    z3=[0,0]           
    for i in originy:
        e=z[i]
        num=len(e)                
        if num>z1[1]:
            z3=z2
            z2=z1
            z1=[i,num]
        elif num>z2[1]:
            z3=z2
            z2=[i,num]
        elif num>z3[1]:
            z3=[i,num]
    w=[]
    for i in originy:
        e=z[i]
        num=len(e)
        if num==z3[1] and i!=z1[0] and i!=z2[0] and i!=z3[0]:
            w.append(i)
    print("Top-3 directors who collaborate with the most actors?\n1st:%s\n2nd:%s\n3rd:%s"%(z1,z2,z3))
    if w!=[]:
        print("並列:",w)
#[5]
elif a==5:
    gen={}
    x=[]
    
    z=[]
    for i in range(1,len(mov)):
        
        b=mov[i][4]
        b1=b.split("|")
        for j in b1:
            if j.lstrip() not in x:
                x.append(j.lstrip())           
    for i in x:
        gen[i]=set()
    for i in range(1,len(mov)):
        y=[]
        b=mov[i][4]
        b1=b.split("|")
        for j in b1:
            y.append(j.lstrip())
#        d=gen[str(b1)]
#    print(y)
        c=mov[i][2]
        c1=c.split("|")        
        for k in y:
#            z.append(k.lstrip())
#        print(z)
            d=gen[k]
            d=d|set(z)
            gen[k]=d
#    print(d)
    gen1=[0,0]#[name,total]
    gen2=[0,0]
    for i in gen:
        f=gen[i]
        num=len(f)
        if num>gen1[1]:
            gen2=gen1
            gen1=[i,num]
        elif num>gen2[1]:
            gen2=[i,num]
    w=[]
    for i in gen:
        f=gen[i]
        num=len(f)
        if num==gen2[1] and i!=gen1[0] and i!=gen2[0]:
            w.append(i)
    print("Top-2 actors playing in the most genres of movies:\n1st:%s\n2nd:%s"%(gen1,gen2))
    if w!=[]:
        print("並列:",w)
#[6]
elif a==6:
   x=[]
   y=[]
   year={}
   for i in range(1,len(mov)):
        b=mov[i][4]
        b1=b.split("|")
        for j in b1:
            if j.lstrip() not in x:
                x.append(j.lstrip())
   for i in x:
       year[i]=[0,3000]                  
   for i in range(1,len(mov)):
       b=mov[i][4]
       c=mov[i][5]
       b1=b.split("|")
       for j in b1:
           y.append(j.lstrip())
       for k in y:
           p=year[k]
           if int(c)>p[0]:
               p[0]=int(c)
           if int(c)<p[1]:
               p[1]=int(c)
           year[k]=p
#差距[name,year gap]           
   gap1=[0,0]
   gap2=[0,0]
   gap3=[0,0]
   for i in range(1,len(mov)):
       b=mov[i][4]
       b1=b.split("|")
       for j in b1:
           if j.lstrip() not in x:
               x.append(j.lstrip())
   for i in x:
       z=year[i]
       con=z[1]-z[0]              
       if con>gap1[1]:
           gap3=gap2
           gap2=gap1
           gap1=[i,num]
       elif con>gap2[1]:
           gap3=gap2
           gap2=[i,num]
       elif con>gap3[1]:
           gap3=[i,num]
   w=[]            
   for i in year:
       z=year[i]
       con=z[1]-z[0]
       if con==gap3[1] and i!=gap1[0] and i!=gap2[0] and i!=gap3[0]:
           w.append(i)
   print("Top-3 actors whose movies lead to the largest maximum gap of years:\n1st:%s\n2nd:%s\n3rd:%s"%(gap1,gap2,gap3))       
   if w!=[]:
       print("並列:",w)
#[7]
elif a==7:
   b=set(["Johnny Depp"])        
   def mtd(b):
       for i in range(1,len(mov)):
           x=[]
           c=mov[i][4]
           c1=c.split("|")
           for y in c1:
               x.append(y.lstrip())
           for z in x:
               if z in b:
                   b=b|set(x)
       return b
   leng=len(b)
   while leng!=len(mtd(b)):
       leng=len(mtd(b))
       b=mtd(b)
   print("All actors who collaborate with Johnny Depp in direct and indirect ways:",b)    