# ex33.py while loop

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("numbers now:", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)



numbers = []

for i in range(0,6):
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("numbers now:", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
