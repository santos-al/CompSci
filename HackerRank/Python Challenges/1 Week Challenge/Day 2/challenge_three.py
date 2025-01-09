def countingSort(arr):
    # Write your code here
    count = [0] * 100  # Step 1: Initialize a list of size 100 with all elements set to 0
    
    for num in arr:  # Step 2: Iterate through the input array
        count[num] += 1  # Step 3: Increment the count at the index corresponding to the number in the array
    
    return count  # Step 4: Return the count array