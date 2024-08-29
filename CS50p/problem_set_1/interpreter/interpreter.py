#Get input from user, Split the string into three parts and assign the corresponding variable x y z
x, y, z = input("Expression: ").split(" ")
x = float(x)
z = float(z)

#Calculate the input and print output
if y == "+":
    print(x + z)
elif y =="-":
    print(x - z)
elif y =="*":
    print(x * z)
elif y =="/":
    print(x / z)

