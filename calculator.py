
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


print("\nSelect operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


choice = input("\nEnter choice (1/2/3/4): ")


if choice == '1':
    result = num1 + num2
    print(f"\n{num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"\n{num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"\n{num1} * {num2} = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"\n{num1} / {num2} = {result}")
    else:
        print("\nError! Division by zero.")
else:
    print("\nInvalid input! Please select a valid operation.")