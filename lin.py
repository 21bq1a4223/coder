def LinearSearch(array,n,x):
    for i in range(0,n):
        if(array[i]==x):
            return i
    return -1
n=int(input("enter size of an array:"))
array=[]
for i in range(n):
    ele=int(input("enter element:"))
    array.append(ele)
x=int(input("enter element to be found:"))
result=LinearSearch(array,n,x)
if(result==-1):
    print("element not found")
else:
    print("element found at index",result)