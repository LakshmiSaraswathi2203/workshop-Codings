def largest(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max = arr[i]
    return max
lst = []
n = int(input("Enter number of elements: "))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
result = largest(lst,n) 
print("The result with largest number in the array is: ",result)   
                