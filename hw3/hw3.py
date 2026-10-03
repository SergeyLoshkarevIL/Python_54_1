def print_list_reverse(lst):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        print("Wrong list")
    else:
        print(lst[::-1])

print_list_reverse([1, 2, 3, 4, 5])
print_list_reverse(None)
print_list_reverse([])
print_list_reverse("hello")
print_list_reverse((1, 2, 3))

print()
#2
def is_valid_point(point):
    if point is None:
        return None
    if isinstance(point, tuple) and len(point) == 0:
        return None

    if not isinstance(point, tuple):
        return False

    if len(point) != 2:
        return False

    for item in point:
        if isinstance(item, bool) or not isinstance(item, (int, float)):
            return False

    return True

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))
print(is_valid_point((1.5, -2)))
print(is_valid_point((True, 5)))

print()

#3

def print_sublist_reverse(lst, start, finish):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        return print("Wrong args")

    if not isinstance(start, int) or isinstance(start, bool):
        return print("Wrong args")

    if not isinstance(finish, int) or isinstance(finish, bool):
        return print("Wrong args")

    if start < 0 or start >= len(lst):
        return print("Wrong args")

    if finish < 0 or finish >= len(lst):
        return print("Wrong args")


    if start > finish:
        return print("Wrong args")

    result = lst[:start] + lst[start : finish + 1][::-1] + lst[finish + 1:]
    print(result)

print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)  # [10, 40, 30, 20, 50, 60]
print_sublist_reverse([1, 2, 3], 0, 2)  # [3, 2, 1]
print_sublist_reverse([1, 2, 3], "0", 2)  # Wrong args
print_sublist_reverse([1, 2, 3], 3, 0)  # Wrong args
print_sublist_reverse(None, 0, 1)  # Wrong args
print_sublist_reverse([], 0, 0)  # Wrong args
print_sublist_reverse([1, 2, 3], 2, 1)  # Wrong args

print()

#4

def get_students_by_grade(students):
    # --- Проверка аргумента ---
    if students is None or not isinstance(students, dict) or len(students) == 0:
        return {}

    # --- Группировка: оценка → [имена] ---
    result = {}
    for name, grade in students.items():
        result.setdefault(grade, []).append(name)

    return result

print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}))
# {90: ['Alice', 'Diana'], 85: ['Bob', 'Charlie']}

print(get_students_by_grade(None))          # {}
print(get_students_by_grade({}))            # {}
print(get_students_by_grade("not a dict"))  # {}
print(get_students_by_grade([1, 2, 3]))     # {}
