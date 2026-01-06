# 電卓
import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

functions = {
    # "+": add(choice_n1, choice_n2),
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator(choice_n1, choice_n2):
    """二つの引数の演算を実行する"""
    return functions[choice_operator](choice_n1, choice_n2)
calc_func = True
while calc_func:
    print(art.logo)
    choice_n1 = float(input("Enter a first number: "))
    calc = True
    while calc:
        choice_operator = input("+\n-\n*\n/\nPlease select an operator: ")
        choice_n2 = float(input("Enter a second number: "))
        answer = float(calculator(choice_n1, choice_n2))
        print(f"{choice_n1} {choice_operator} {choice_n2} = {answer}")
        continue_flag = input("Press 'y' to continue calculating, "
                              "or 'n' to start a new calculation"
                              "or 's' to stop a calculation: ").lower()
        if continue_flag == "y":
            choice_n1 = answer
        elif continue_flag == "n":
            calc = False
            print("\n" * 20)
        else:
            calc = False
            calc_func = False
            print("Calculator halt")

# whileではなく、関数を使用した場合
"""            
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
"""

