def largest(arr,n):
    min=arr[0]
    for i in range(1,n):
        if arr[i]<min:
            min = arr[i]
    return min
lst = []
n = int(input("Enter number of elements: "))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
result = largest(lst,n) 
print("The result with smallest number in the array is: ",result)
