def total(*args):
    print(type(args), args)
    return sum(args)

print(total(1,3,2))
print(total(10,11))
print(total(12,20,30,50))
print(total())
print()

def print_score(students, *scores):
    print(f"Students:{students}, Scores:{scores}")

print_score("Kristina", 30, 20, 45)
print_score("Alex",60)


def check_status_codes(*codes):
    for code in codes:
        assert code == 200

print(check_status_codes(200,200,200))
#print(check_status_codes(200,400,500))