# Exercise 21: functions can return something
#Attention: Replace tab by space

def add(a,b):
    print("Adding {a} + {b}")
    return a+b

def subtract(a,b):
    print("SUBTRACTING {a} - {b}")
    return a-b

def multiply(a,b):
    print("MULTIPLING {a} * {b}")
    return a*b

def divide(a,b):
    print("DIVIDING {a} / {b}")
    return a/b


print(f"Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78,5)
weight = multiply (90,2)
IQ = divide(100,6)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {IQ}")


# A puzzle for the extra credit, type it in anyway.
print(f"Here is a puzzle.")

what = add(age, subtract(multiply(weight, divide(IQ,2)), height))

print(f"That becomes:", what, "Can you do it by hand?")
