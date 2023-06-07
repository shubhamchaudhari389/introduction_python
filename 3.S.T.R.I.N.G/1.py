s =input("Enter some String:")
i =0
for x in s:
    print("The character present at Postive index {} and at aEgative index{} is {}".format(i,i-len(s),x))
    i =i+1