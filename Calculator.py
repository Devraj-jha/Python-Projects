while True:
    print("____________________________")
    print(" ######## Calculator ######## ")

    num1 = input("Enter First number(or q to quit): ")
    if num1 == 'q':
        break
    operator = input("Enter your operator (+, - , *, /,pow, undroot):  ")

    num2 = input("Enter 2nd number: ")
   
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == '0':
                print("Error can't divide by 0,")
            continue
            result = num1 / num2
        elif operator == 'pow':
            result = num1 ** num2
        elif operator == 'undroot':
            result = num1 ** ( 1 / num2)
        else: 
            print(" Invaild operator !!! Try again")
            continue

        print(f"Result: {result}\n")
    except ValueError:
        print("Please enter valid thing and try again \n")
    