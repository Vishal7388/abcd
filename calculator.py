first = int(input("Enter your first number : "))
operator = (input("Enter the operator (+,-,/,*,%) : "))
second = int(input("Enter your second number : "))
if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)    
elif operator == "*":
    print(first*second)   
elif operator == "/":
    print(first/second)
elif operator == "%":
    print(first%second)
else:
    print("Envalid number")