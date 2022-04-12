number = int(input("Please input a number: "))
divisors = [i for i in range(1, number+1) if number % i == 0]

print("Divisor(s): ")
print(divisors)