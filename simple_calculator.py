   while True:
       num1 = int(input("Enter first number: "))
       num2 = int(input("Enter second number: "))
       op = input("Enter operation (+, -, *, /, %): ")
       
       if op == '+':
           print(f"Result: {num1 + num2}")
       elif op == '-':
           print(f"Result: {num1 - num2}")
       elif op == '*':
           print(f"Result: {num1 * num2}")
       elif op == '/':
           print(f"Result: {num1 / num2}")
       elif op == '%':
           print(f"Result: {num1 % num2}")
       else:
           print("Invalid operation")
       
       cont = input("Continue? (yes/no): ")
       if cont.lower() != 'yes':
           break
