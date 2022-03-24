def newtonSqrt(n, base):
    approx_root = 0.5 * n
    for i in range(base):
        betterapprox = 0.5 * (approx_root + n/approx_root)
        approx_root = betterapprox
    return betterapprox

num1=int(input("Enter any number: "))
base1=int(input("Enter base: "))

print("The square root:",newtonSqrt(num1,base1))
