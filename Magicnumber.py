n=int(input("enter a number is magic number or not:"))


while n>9:
    sum=0
    while n!=0:
        num=n%10
        sum+=num
        n=n//10
    n=sum
if sum==1:
    print("Magic number")
else:
    print("Not an magic number")


