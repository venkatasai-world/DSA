num=int(input("enter a number to test wheather a number is strong or not: "))
temp=num
sum=0
while temp!=0:
    n=temp%10
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    sum+=fact
    temp=temp//10

if sum==num:
    print("strong number")
else:
    print("not a strong number")
        

