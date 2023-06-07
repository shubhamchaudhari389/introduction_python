s=input("Enter The Main String:")
subs=input("Enter Sub String:")
try:
    n=s.index(subs)
except ValueError:
    print("substring Not found")
else:
    print("substring found")