#Q. String objects are immutable then how we can change the content by
#using replace() method.
s="abab"
s1=s.replace("a","b")
print(s,"is availabe at:",id(s))
print(s1,"is available at:",id(s1))