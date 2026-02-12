n = int(input("Enter a number to check happy or not: "))

while n > 9:
    s = 0
    while n != 0:
        digit = n % 10
        s += digit * digit
        n //= 10
    n = s

if n == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")
