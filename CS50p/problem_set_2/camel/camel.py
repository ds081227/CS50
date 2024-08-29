camelcase = input("camelCase: ")
print("snake_case: ",end="")
for i in camelcase:
	if i.isupper():
		#No need to use f string here, can just be print("_" + i.lower(),end = "")
		print("_" + i.lower(), end="")
	else:
		print (i, end="")
print()
