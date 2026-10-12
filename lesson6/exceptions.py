# def div_int(a,b):
#     return a/b
# print("start program")
# result = div_int(10,0)
# print(result)
# print("end program"

print("hello world")
try:
    result = 10/0
    print(result)
except Exception as e:
    print("an error occurred: e")
print("bye")

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result: ",result)
except ValueError:
    print("error: please enter a valid number")
except ZeroDivisionError:
    print("error: cannot divide by zero")

def is_number(text):
    try:
        float(text)
        return True
    except (TypeError, ValueError):
        return False
print(is_number("314"))
print(is_number("3.14"))
print(is_number("3,14"))
print(is_number("kris"))
print(is_number(None))

print()

try:
    value = int("39")
except ValueError:
    print("error: please enter a valid number")
else:
    print(value)
finally:
    print("finally")