numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("List of numbers:")
print(numbers)

print("\nSquare of every number of the provided list:")
square_numbers = list(map(lambda x: x ** 2, numbers))
print(square_numbers)

print("\nCube of every number of the provided list:")
cube_numbers = list(map(lambda x: x ** 3, numbers))
print(cube_numbers)