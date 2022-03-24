def power(x,n):
    if n==0:
        return 1
    else:
        return x * power(x, n-1)

base = float(input("Enter value of base: "))
exponent = int(input("Enter value of exponent: "))

result = power(base, exponent)

print("Result is:", result)