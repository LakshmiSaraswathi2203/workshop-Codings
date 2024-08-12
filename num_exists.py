def num_exists(arr,n,num):
    for i in range(0,n):
        if(arr[i]==num):
            print("True")
            break
lst = []
n = int(input("Enter the number of elements: "))
print("Enter the elements")
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
num = int(input("Enter a number to search.."))    
num_exists(lst,n,num) 
