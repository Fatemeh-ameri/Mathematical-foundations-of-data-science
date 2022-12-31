number_one = int(input("enter number 1: "))
number_two = int(input("enter number 2: "))

def gdc(a, b):
    if(b == 0):
        return a
    else:
        return gdc(b, a % b)

print("The gcd of {} and {} is : ".format(number_one, number_two), gdc(number_one, number_two))