first_number = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

if operator == "+":
    problem = str(first_number) + "+" + str(second_number)
    result = first_number + second_number
    print(result)
elif operator == "-":
    problem = str(first_number) + "-" + str(second_number)
    result = first_number - second_number
    print(result)
elif operator == "*":
    problem = str(first_number) + "*" + str(second_number)
    result = first_number * second_number
    print(result)
elif operator == "/":
    problem = str(first_number) + "/" + str(second_number)
    result = first_number / second_number
    print(result)
else:
    print("Invalid operator. Please try again.")

calculator_database = open("database.txt", "a")

calculator_database.write("--------------------" + "\nProblem: " + str(problem) + "\nResult: " + str(result) + "\n--------------------" + "\n" + "\n")

calculator_database.close()
