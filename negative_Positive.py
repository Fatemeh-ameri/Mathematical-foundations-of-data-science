# Determining whether a number is negative or positive

number = float(input("enter any number you want:"))

def negative_Positive(number):
    if number == 0:
        return "It's Zero"
    elif number > 0:
        return "It's Positive"
    else:
        return "It's Negative"   

print(negative_Positive(number))
    