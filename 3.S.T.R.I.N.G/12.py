# Q. Program to display all positions of substring in a given main string
s=input("Enter The String:")
subs=input("Enter sub string:")
flag=False
pos=-1
n=len(s)
while True:
    pos=s.find(subs,pos+1,n)
    if pos==-1:
        break
    print("Found at Position",pos)
    flag=True
if flag==False:
    print("Not Found")