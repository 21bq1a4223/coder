s=input("enter any string:")
vowels=['a','e','i','o','u']
c=0
for i in str(vowels):
    if i in s.lower():
        c+=1
if c==5:
    print("string contains all vowels")
else:
    print("string doenot contains all vowels")