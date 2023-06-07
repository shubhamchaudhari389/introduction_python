#Q. Write a program to access each character of string in forward and backward direction
"""s ="Learning Python is very easy !!!"
n =len(s)
print(n)
i=0
print("forward Direction")
while i<n:
    print(s[i],end='')
    i +=1
print("Backword Direction")
i=-1
while i>=-n:
    print(s[i],end='')
    i=i-1"""

s="Learning Python is very easy !!!"
print("Forword Direction \n")

for i in s:
    print(i,end="")

print("Forword Direction")
for i in s[::]:
    print(i,end="")

print("Backword Direction")
for i in s[::-1]:
    print(i,end="")
    

