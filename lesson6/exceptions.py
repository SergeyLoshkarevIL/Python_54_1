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