print("enter * to exit")
a=[]
c,d,e=0,0,0
for i in range(0,100):
   b=input ("enter the element:") 
   if(b== '*'):
       break
   else:
      a.append(b)
for i in a:
    if(i.isupper()): 
        c+=1
    elif(i.islower()):
        d+=1
    elif(i.isnumeric()):
        e+=1
print("no of lowercase element",d)
print("no of uppercase element",c) 
print("no of numbers ",e)
