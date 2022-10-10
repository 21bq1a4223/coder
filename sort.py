def is_sorted(n):
    flag='True'
    for i in range(len(n)-1):
        if n[i]<n[i+1]:
               flag='True'
        else:
               flag='false'
               break
    return(flag)
n=[1,2,7,4,5]
flag=is_sorted(n)
if flag=='True':
       print("True,the list is sorted")
else:
       print("False,the list is not sorted")