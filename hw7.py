import re


def is_positive_less_than_300(value:300):
    pattern = r"^([1-9][0-9]{0,1}|[1-2][0-9]{2})$"
    return bool(re.fullmatch(pattern, str(value)))

print(is_positive_less_than_300("1"))     # True
print(is_positive_less_than_300("15"))    # True
print(is_positive_less_than_300("99"))    # True
print(is_positive_less_than_300("100"))   # True
print(is_positive_less_than_300("299"))   # True

print(is_positive_less_than_300("0"))     # False
print(is_positive_less_than_300("300"))   # False
print(is_positive_less_than_300("-5"))    # False
print(is_positive_less_than_300("3.14"))  # False
print(is_positive_less_than_300("Abc"))   # False

print()


#2
def is_number_from_1_to_255(value):
    return re.fullmatch(r"[1-9]\d?|1\d\d|2[0-4]\d|25[0-5]",value) is not None
print(is_number_from_1_to_255("300"))
print(is_number_from_1_to_255("12"))
print(is_number_from_1_to_255("asd"))
print(is_number_from_1_to_255("-5"))

print()

#3

def is_israel_mobile(phone: str) -> bool:
    pattern = r"^(?:\+972|0)?5[0-9]-?[0-9]{2}-?[0-9]{2}-?[0-9]{3}$"
    return bool(re.fullmatch(pattern, str(phone)))

print (is_israel_mobile("0543401398"))

print(is_israel_mobile("0541234567"))     # True
print(is_israel_mobile("054-1234567"))    # True
print(is_israel_mobile("+97254-123-4567"))# True
print(is_israel_mobile("058-12-34-567"))  # True

# Неподходящие:
print(is_israel_mobile("54-1234567"))     # False (нет кода 0 или +972)
print(is_israel_mobile("054--12-4567"))   # False (двойной дефис)
print(is_israel_mobile("+972054-123-4567"))# False (ноль после +972)
print(is_israel_mobile("97254-123-4567")) # False (нет плюса перед 972)
print()

#4
def is_valid_time(time):
    # Паттерн для формата HH:MM (от 00:00 до 23:59):
    # (?:[01][0-9]|2[0-3]) — часы от 00 до 23 (две цифры обязательны)
    # : — разделитель
    # [0-5][0-9] — минуты от 00 до 59
    pattern = r"^(?:[01][0-9]|2[0-3]):[0-5][0-9]$"
    return bool(re.fullmatch(pattern, str(time)))

print(is_valid_time("00:00"))     # True
print(is_valid_time("09:30"))     # True
print(is_valid_time("14:45"))     # True
print(is_valid_time("23:59"))     # True

# Не подходят:
print(is_valid_time("24:00"))     # False (часы больше 23)
print(is_valid_time("12:60"))     # False (минуты больше 59)
print(is_valid_time("8:30"))      # False (нет ведущего нуля у часов)
print(is_valid_time("123:45"))    # False (слишком много цифр в часах)
print(is_valid_time("12-30"))     # False (неверный разделитель)

print()


#5

def is_israel_car_number(number):
    # Паттерн поддерживает два формата:
    # \d{2}-\d{3}-\d{2}   — 7-значный формат (XX-XXX-XX)
    # \d{3}-\d{2}-\d{3}   — 8-значный формат (XXX-XX-XXX)
    pattern = r"^(\d{2}-\d{3}-\d{2}|\d{3}-\d{2}-\d{3})$"
    return bool(re.fullmatch(pattern, str(number)))

print(is_israel_car_number("12-345-67"))    # True
print(is_israel_car_number("99-999-99"))    # True
print(is_israel_car_number("123-45-678"))   # True
print(is_israel_car_number("456-78-901"))   # True

# Не подходят:
print(is_israel_car_number("12345678"))     # False (нет дефисов)
print(is_israel_car_number("12:345:67"))    # False (неверные разделители)
print(is_israel_car_number("1-234-56"))     # False (неверное количество цифр в блоках)
print(is_israel_car_number("1234-56-78"))   # False (первый блок длиннее 3 цифр)

print()