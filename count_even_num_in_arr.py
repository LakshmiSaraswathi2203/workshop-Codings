def CountingEvenNum(arr,n):
    even_count = 0
    for i in range(n):
        if(arr[i]%2==0):
            even_count+=1

    return even_count
lst = []
n = int(input("enter number of elements in array"))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
result = CountingEvenNum(lst,n)
print("the result is: ",result)    
        