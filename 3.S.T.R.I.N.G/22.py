s=input("Enter Any Character:")
if s.isalnum():
    print("Alpha Numeric character")
    if s.isalpha():
        print("Alphabet")
        if s.islower():
            print("Lower Case Of Aplhabet")
        else:
            print("Upper Case of Alphabet")
    else:
        print("it is digit")
elif s.isspace():
    print("It is space character")
else:
    print("Non Space Special Character")