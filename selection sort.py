#selection sort is algorithm used to sorting the array from lower to higer or higer to lower
#sort

import sys
A = [64, 25, 12, 32, 78, 56]

#traverse through all array element

for i in range(len(A)):
    #lets find the minimum element exist in array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx]>A[j]:
            min_idx = j
    #swap the found minimum element with the first element
    A[i], A[min_idx] = A[min_idx], A[i]

print("sorted array are:")
#print all elements by index
for i in range(len(A)):
    print("%d" %A[i], end=" ")

print("\n")
