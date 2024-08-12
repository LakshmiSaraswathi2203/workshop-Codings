def sumOfOdd(arr,n):
    sum = 0
    for i in range(0,n):
        if((arr[i]%2)!=0):
            sum += arr[i]
    return sum        
lst = []
n = int(input("Enter the number of elements: "))
print("Enter the elements")
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
result = sumOfOdd(lst,n) 
print ("The sum of odd elements occured is: ", result)    
