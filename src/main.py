# Constants for messages
MENU_TEXT = """
--- Calculator Menu ---
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
"""

PROMPT_CHOICE = "Choose an option (1-5): "
PROMPT_NUM1 = "Enter first number: "
PROMPT_NUM2 = "Enter second number: "
ERROR_DIV_ZERO = "Error: Division by zero!"
ERROR_INVALID_CHOICE = "Invalid choice!"
GOODBYE_MSG = "Goodbye!"
RESULT_MSG = "Result: {}"

# Calculator loop
while True:
    print(MENU_TEXT)
    choice = input(PROMPT_CHOICE)

    if choice == "5":
        print(GOODBYE_MSG)
        break

    # Get numbers from user
    try:
        num1 = float(input(PROMPT_NUM1))
        num2 = float(input(PROMPT_NUM2))
    except ValueError:
        print("Error: Please enter a valid number!")
        continue

    # Perform calculation
    if choice == "1":
        print(RESULT_MSG.format(num1 + num2))
    elif choice == "2":
        print(RESULT_MSG.format(num1 - num2))
    elif choice == "3":
        print(RESULT_MSG.format(num1 * num2))
    elif choice == "4":
        if num2 == 0:
            print(ERROR_DIV_ZERO)
        else:
            print(RESULT_MSG.format(num1 / num2))
    else:
        print(ERROR_INVALID_CHOICE)
