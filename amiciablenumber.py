one=int(input("enter the first number in the pair"))
two=int(input("enter the second number in the pair"))

sum1=0
sum2=0

for i in range(1,one):
    if one%i==0:
        sum1+=i
for i in range(1,two):
    if two%i==0:
        sum2+=i

if two==sum1 and one==sum2:
    print("Amiciable Number")
else:
    print("Not an Amiciable Number")
