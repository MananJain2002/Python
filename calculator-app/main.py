from art import logo

print(logo)

def calculate(num1, num2, operator):

    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2 
        case '*':
            return round(num1 * num2, 5)
        case '/':
            return round(num1 / num2, 5)

switch_on = True

while switch_on:

    while True:
        try:
            num1 = float(input("What's the first number?: "))
            break
        except:
            print("Please enter a valid number")

    should_continue = True
    while should_continue: 
    
        print("+\n-\n*\n/")
        operators = '+-*/'
        operator = '_'

        while operator not in operators:
            operator = input("Pick an operator: ")

        while True:
            try:
                num2 = float(input("What's the next number?: "))
                break
            except:
                print("Please enter a valid number")

        num1 = calculate(num1, num2, operator)
        
        should_continue = True if input(f"Type 'y' to continue calculating with {num1}, or type 'n' to start a new calculation: ").lower() == 'y' else False