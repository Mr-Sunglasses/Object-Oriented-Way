def square(number):

    return number ** 2

try:
    x = square(12)
    print(x)
except TypeError:
    print(f"Required type {type(1)} ")
finally:
    print("This will run Always")