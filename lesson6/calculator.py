#only performs calculator
def calculator(a:float, b:float, operator:str):
    if operator=="+":
        return a+b
    elif operator=="-":
        return a-b
    elif operator=="*":
        return a*b
    elif operator=="/":
        return a/b
    else: raise ValueError("invalid operator")

#parsing convert string into numbers
def pars(a_str: str, b_str: str, operator:str):
    a = float(a_str)
    b = float(b_str)
    return calculator(a,b,operator)

#dialog
def run():
    try:
        a = input("Enter a first number: ")
        b = input("Enter a second number: ")
        operator = input("Enter actions operator (+,-,-*,/): ")
        result = pars(a,b,operator)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"invalid input: {e}")
    except ZeroDivisionError as e:
        print(f"division by zero: {e}")
run()


