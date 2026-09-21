#task1
def clean_name(name):
    return name.strip().title()

print(clean_name("  anna smith   "))
print(clean_name("DAVID COHEN"))


#task2
def normalize_email(email):
    return email.strip().lower()

print(normalize_email(" Anna.smith@Example.COM"))


#task3
def is_python_file(filename):
    return filename.lower().endswith('.py')

print(is_python_file('lesson.py'))
print(is_python_file('HOMEWORK.PY'))
print(is_python_file('notes.txt'))


#task4
def fix_message(message):
    return message.replace('bad', 'good')

message = 'bad weather, bad mood'
result = fix_message(message)

print(result)

#task5
def count_letter(text, letter):
    return text.lower().count(letter.lower())

print(count_letter('Programming', 'g'))
print(count_letter('Mississippi', 'I'))


#task6
def create_login(first_name, last_name):
    first_name = first_name.strip().title()
    last_name = last_name.strip().title()
    return first_name + '.' + last_name

print(create_login('Anna', 'SMITH'))


#task6_2
def create_login(first_name, last_name):
    return f"{first_name.strip().lower().title()}.{last_name.strip().lower().title()}"

print(create_login('Anna', 'SMITH'))


#task7
def split_name(full_name):
    return full_name.strip().split()

print(split_name('  Anna    Smith  '))


#task8
def check_password(password):
    if len(password) < 8:
        return False
    if " " in password:
        return False
    if password.isalpha():
        return False
    return True

print(check_password('python123'))
print(check_password('python'))
print(check_password('python 123'))
