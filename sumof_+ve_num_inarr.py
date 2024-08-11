def sumofPosnum(arr,n):
    sum=0
    for i in range(n):
        if(arr[i]>0):
            sum +=arr[i]
    return sum
lst = []
n = int(input("enter number of elements in array: "))
print("Enter the elements: ")
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
result = sumofPosnum(lst,n)
print("the sum is: ",result)