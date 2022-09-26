a=int(input("enter the no,of new loaves sold:"))
b=int(input("enter the no.of one day loaves sold:"))
if(a<0):
    print("enter the no greater than the 0")
else:
    c=a*185
    d=(b*185)*60/100
    print("regular price=185")
    print("amount of new loaves",float(c))
    print("amount of day old loaves",float(d))
    print("total amount",float(c+d))
