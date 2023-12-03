# Compulsory Task 1

# Perform calculations or print previous calculations from equations.txt.


# Defined a function called "calculate" which is used to calculate the user's equation correctly.
# Set up a menu for the user to select an option of what they would like to do.
# Used a try-except block to ensure the user inputs a valid option from the menu given.
# Exceptions should be caught and the user should be asked to input a valid menu option again.

def calculate(num1, operand, num2,):
    if operand == "+":
        equation = num1 + num2
        return equation

    elif operand == "-":
        equation = num1 - num2
        return equation

    elif operand == "*":
        equation = num1 * num2
        return equation

    elif operand == "/":
        equation = num1 / num2
        return equation

    else :
        print("Please enter a valid operator!")

menu_options = 0

while menu_options != 3 :
    try:
        print("\n1.   Perform a calculation.")
        print("2.   Print all previous equations.")
        print("3.   Exit.")

        menu_options = int(input("Please select Menu Option (1-3): "))


        #Set out what should happen if the user selects menu option 1.
        '''If option 1 is selected to perform a calculation, the output file called "equations.txt"
        should be opened in append mode. The user should be able to input a valid first number, a 
        valid second number, as well as a valid operator to be used in performing the calculation.
        Exceptions must be caught and explained to the user, who should then be able to try to 
        either enter the correct input again, or try to re-perform the calculation again, depending
        on where the exception has occurred. Once all inputs have been entered correctly, the 
        calculation should be performed and then stored in equation form in "equations.txt". The 
        output file should then be closed and the user should be able to select a menu option again.'''
        #Set out what should happen if the user selects menu option 2.
        '''If option 2 is selected to print all previous equations, the output file called 
        "equations.txt" should be opened in read mode. An exception should be raised if the output
        file does not exist, and the user should be able to select a menu option again. If the 
        output file exists, the equations stored in the output file should then be read and printed
        out. The output file should then be closed and the user should be able to select a menu 
        option again.'''
        #Set out what should happen if the user selects menu option 3.
        '''If option 3 is selected to exit the application, a 'Goodbye' message should print for 
        the user.'''

        if menu_options == 1 :
            while True:
                try:
                    output_file = open("equations.txt", "a+")
                    print("Perform a calculation:")

                    while True:
                        try:
                            num1 = int(input("Please enter the first number for your equation: "))
                    
                            break
                        except Exception:
                            print("Please enter a valid first number for your equation!")


                    while True:        
                        try:    
                            num2 = int(input("Please enter the second number for your equation: "))
                    
                            break
                        except Exception:
                            print("Please enter a valid second number for your equation!")


                    while True:
                        try:
                            operand = input("Please enter a valid operator (+,-,*,/) for your equation: ")
                            
                            if operand == "+" :
                                equation = calculate(num1, operand, num2)

                            elif operand == "-" :
                                equation = calculate(num1, operand, num2)

                            elif operand == "*" :
                                equation = calculate(num1, operand, num2)

                            elif operand == "/" :
                                try:
                                    if num2 ==0 :
                                        raise ZeroDivisionError(f"{num1} cannot be divided by {num2}. Please try again.")

                                    else :
                                        equation = calculate(num1, operand, num2)

                                    break
                                except ZeroDivisionError:
                                    print(f"{num1} cannot be divided by {num2}. Please try again.")

                            else :
                                raise Exception("Please select either a \"+\", \"-\", \"*\" or \"/\".")

                            break
                        except Exception:
                            print("Please select either a \"+\", \"-\", \"*\" or \"/\".")

                    if num2 ==0 and operand == "/" :
                        print("Your equation could not be calculated.")

                    else :    
                        print(f"The answer to your equation is {equation}.")

                        output_file.write(f"{num1} {operand} {num2} = {equation}\n")
                        output_file.close()

                    break
                except Exception:
                    print("Please try to perform your calculation again!")


        elif menu_options == 2 :
            while True:
                try:
                    print("Print all previous equations:")
                    output_file = open("equations.txt", "r")
                    equation_history = output_file.read()
                    print(equation_history)
                    output_file.close()

                    break
                except FileNotFoundError:
                    print("File \"equations.txt\" does not exist!")
                    print("Sorry. There are no previous equations to be printed.")
                    break


        elif menu_options == 3 :
                    print("Thank you for using this application. Goodbye!")


        else :
            raise Exception("Please select a valid menu option!")
   
    except Exception:
        print("Please select a valid menu option!")