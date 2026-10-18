import re

text = "The status is passed"
result = re.search("passed", text)
print(result)
print(result.group())

text2 = "passed: test registration"
text3 = "test registration: passed"
print(re.match("passed",text2))
print(re.match("passed",text3))

print()

print(re.search("d.g","dog"))
print(re.search("d.g","dig"))
print(re.search("d.g","dg"))

print(re.search("^Test","Test is start"))
print(re.search("^Test","Start is test"))

print(re.search(r"ab+c","ac"))
print(re.search(r"ab+c","abc"))
print(re.search(r"ab+c","abc"))

print(re.search(r"colou?r","color"))
print(re.search(r"colou?r","colour"))
print(re.search(r"colou?r","colouur"))

print(re.search(r"\d{3}","13"))
print(re.search(r"\d{3}","15666638"))
print(re.search(r'\d{2,4}',"123456"))
print(re.search(r'\d{3,4}',"323"))