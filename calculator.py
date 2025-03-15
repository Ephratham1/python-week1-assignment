num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("Which operation would you like to peform?")
operator = input("enter arithmetic operator to execute like +, *, /, - : ")

results = 0
if  operator == "+":
 results = num1 + num2
elif  operator == "-":
 results = num1 - num2
elif operator == "*":
 results = num1 * num2
elif  operator == "/":
 results = num1 / num2
else: print("invalid arithmetic operator entered")

print(num1 ,operator, num2, "=", results)

