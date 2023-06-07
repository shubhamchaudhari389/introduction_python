# Write A program To find Biggest of given 3 number

n1 =int(input("Entre The First Number:"))
n2 =int(input("Entre The Second Number:"))
n3 =int(input("Entre The Third Number:"))

if n1>n2 and n1>n3:
    print("Biggest Number is:",n1)
elif n2>n3 and n2>n1:
    print("Biggest Number Is:",n2)
else:
    print("Biggesr No is:",n3)