def print_configuration(**kwargs):
    print(type(kwargs), kwargs)

print_configuration(browser = "safari", headless = True, timeout = 10)