num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
operator = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, operator , num2, "is", result)
