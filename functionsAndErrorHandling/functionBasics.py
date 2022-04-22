def square(number):
    return number * number


print(square(4))

# Positional Argument
print(square(number=12))


# Default Parameter

def Age(age=18):
    return f"Your are is {age}"


print(Age(age=22))
