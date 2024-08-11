#for addition
def add(*args):
    return sum(args)

#for subtraction
def minus(*args):
    if len(args) == 0:
        return 0
    
    result = args[0]
    
    for num in args[1:]:
        result -= num
    return result

#for multiplication
def mul(*args):
    result = 1
   
    for num in args:
        result *= num
    return result

#for division
def div(*args):
    if len(args) == 0:
        return "unidentified"

    result = args[0]

    for num in args[1:]:
        if num == 0:
         return "divide by 0 is not possible, please choose a number other than 0"
        result /= num
    return result

#for modulus
def mod(*args):
    if len(args) < 2:
        return " At least two numbers are required for modulus"
    
    result = args[0]

    for num in args[1:]:
        if num == 0:
            return "division by zero is not possible for modulus"
        result %= num
    return result

#defining the calculator function to do the calculations
def calculator():

    #using a while loop for calculator
    while True:

        # Prompt the user for input
        operation = input("Enter the operation (add = +, subtract = -, multiply = *, divide = /, modulus = %): ").strip().lower()

        #break if
        if operation == 'exit':
            print("Exiting the calculator. Sayonara!")
            break
        
        # this helps to send users a message to provide a suitable character
        if operation not in ['+', '-', '*', '/', '%']:
            print("please use the given character in the prompt or enter exit to exit the program")
            continue

        #input numbers of not exit and continue with calculations
        numbers = input("Enter the numbers for your calculations, separated by spaces: ").strip().split()
        
        # Convert the input strings to floats or integers
        try:
            args = [float(num) for num in numbers]
        except ValueError:
            print("Please enter only numbers.") 
            continue

        # Call the add function with *args
        if operation == '+':
            result = add(*args)

        elif operation == '-':
            result = minus(*args)
        
        elif operation == '*':
            result = mul(*args)

        elif operation == '/':
            result = div(*args)
        
        elif operation == '%':
            result = mod(*args)

        else:
            print("unsupported operation, please use add, subtraction, multiplication, or division")
            continue #skip to the next iteration of the loop

        # Display the result
        print(f"The result of the calculation is: {result}")

        #ask the user if they want to continue with the operations and calculations

        continue_calculation = input("do you wist to choose another operatopn? if yes type - yes, else type - no").strip().lower()
        if continue_calculation != 'yes':
            print("exiting the calculator, Sayonara!")
            break

# Example usage
calculator()