# Determine sum of digits

number = int(input("Enter a number:"))
if number < 0:
    number = -number
sum = 0
while(number>0):
    dig = number%10
    sum = sum+dig
    number=number//10
print("The total sum of digits is:",sum)       