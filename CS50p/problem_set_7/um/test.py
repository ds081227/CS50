import re
s = input("Sentence: ")
m = re.findall(r"\bum\b",s, re.IGNORECASE)
print(m)



