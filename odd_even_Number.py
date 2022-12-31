# Determining whether a number is even and odd

number = int(input("enter any number you want:"))

def odd_even(n):
    if n == 0:
        return("Zero is neither even nor odd.")
    elif n%2 == 0:
        return("even")
    else:
        return("odd")      

print(odd_even(number))