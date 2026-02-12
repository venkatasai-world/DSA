n=int(input("enter a number to check the perfect number or not:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i

if n==sum:
    print("Perfect number")
else:
    print("Not a perfect number")
