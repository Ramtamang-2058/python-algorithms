#binary search algorithm
# arr --> array, low--> zero index array and high--> higher index array, x--> value

def binary_search(arr, low, high, x):
    if high >=low:
        #find the mid value of array
        mid = (high + low)//2
        #if equals to x then its value
        if arr[mid]==x:
            return mid
        elif arr[mid] > x:
        #if mid is greater than x then it lies right side otherwise left
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x=2
result = binary_search(arr, 0, len(arr)-1, x)
if result != -1:
    print("The binary index of the number is: "+ str(result))
else:
    print("number not found in array !")
