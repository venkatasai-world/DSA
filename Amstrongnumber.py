num=int(input('enter a number to check whether given number is armstrong or not:'))
n=len(str(num))
temp=num
ams=0
while temp!=0:
    n1=temp%10
    ams = ams + (n1 ** n)
    temp=temp//10

if num==ams:
    print("Armstrong Number")
else:
    print("Not an Armstrong number")
