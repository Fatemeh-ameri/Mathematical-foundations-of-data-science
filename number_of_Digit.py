# Determine number of digits

number = float(input("enter any number you want:"))
def number_of_Digit(number):
    ex_Number = number
    if number < 0:
        number = - number
    counter = 0
    while(number >0):
        counter = counter+1
        number = number//10    
    return "The number of digits in the number {} is equal to {}.".format(ex_Number, counter)

print(number_of_Digit(number))            
    