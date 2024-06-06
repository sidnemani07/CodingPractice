def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer -1
        for i in range(first, last):
            offset = i -first
            top = matrix[first][i]
            #left to top
            matrix[first][i] = matrix[last-offset][first]
            #bottom to left
            matrix[last-offset][first] = matrix[last][last-offset]
            #right to bottom
            matrix[last][last-offset] = matrix[i][last]
            #top to right
            matrix[i][last] = top

def main():
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    rotate_matrix(matrix)
    print(matrix)

if __name__ == "__main__":
    main()