#Prompts user for the name of a variable
#Identify the separator(Capital Letters) and split it
#Output corresponding name in snake case(print and add separator _)
camelcase = input("camelCase: ")
underscores = "_"
for i in camelcase:
	if i.isupper():
		print(i"_".lower(),end="")
	else:
		print (i, end="")
