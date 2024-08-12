def Findocc(arr,key,n):
    count =0
    for i in range(0,n):
        if(arr[i]==key):
            count+=1
    return count
lst = []
n = int(input("Enter the number of elements: "))
print("Enter the elements")
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
key = int(input("enter the element to search for its occurance"))    
result = Findocc(lst,key,n) 
print ("The number of times the element occured is: ", result)
