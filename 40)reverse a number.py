n = int(input("Enter the integer number: "))   
rev = 0 
  
while (n > 0):  
    rem = n % 10  
    rev= (rev * 10) + rem 
    n = n // 10 
print("The reverse number is : {}".format(rev))  
