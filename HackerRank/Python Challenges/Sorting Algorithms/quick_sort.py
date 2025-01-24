def quick_sort(arr: list) -> list:
    if len(arr) <= 1:  # Base case: arrays with 0 or 1 element are already sorted
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the pivot element
        
        # Initialize lists for partitioning
        left = []
        middle = []
        right = []
        
        # Partition the array based on the pivot
        for x in arr:
            if x < pivot:
                left.append(x)  # Elements less than pivot
            elif x == pivot:
                middle.append(x)  # Elements equal to pivot
            else:
                right.append(x)  # Elements greater than pivot
        
        # Recursively sort and combine the results
        return quick_sort(left) + middle + quick_sort(right)

# Example usage
numbers = [3, 6, 8, 10, 1, 2, 1]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)  # Output: [1, 1, 2, 3, 6, 8, 10]