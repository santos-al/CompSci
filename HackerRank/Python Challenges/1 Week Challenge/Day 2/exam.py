arr = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]

# Answer is 119
def flippingMatrix(matrix):
    # Write your code here
    size = len(matrix) 
    sum = 0

    for i in range(size // 2): 
        for j in range(size // 2): 
            sum += max(matrix[i][j], matrix[size - i - 1][j], matrix[size - i - 1][size - j - 1], matrix[i][size - j - 1])
    return sum

print(flippingMatrix(arr))