n=int(input("enter a number to check whether a number is ugly or not"))

temp=n
while(temp%2==0):
    temp//=2
while(temp%3==0):
    temp//=3
while(temp%5==0):
    temp//=5
if temp==1:
    print("Ugly number")
else:
    print("Not an ugly number")    

