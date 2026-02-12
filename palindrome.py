num=int(input("enter a number to check palindrome or not:\n"))
temp=num
rev=0
while temp!=0:
    n1=temp%10
    rev=rev*10+n1
    temp//=10

if sum==num:
    print("Palindrome number")
else:
    print("Not a palindrome number")
    