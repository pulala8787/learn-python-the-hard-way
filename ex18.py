# this one is like your scripts with argv
def print_three(*args):
    arg1, arg2, arg3 = args
    print (f"arg1: {arg1}, arg2: {arg2}, arg3:{arg3}")

# ok, that *args is actually pointless, we can just do this
def print_three_again(arg1, arg2, arg3):
    print ("arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")

# this just takes one argument
def print_one(arg1):
    print ("arg1: {arg1}")

# this one takes no arguments
def print_none():
    print ("I got nothin'.")


print_three("Tammy", "Shaw", "Happy")
print_three_again ("Zed", "Shaw", "Snoop")
print_one("First!")
print_none()
