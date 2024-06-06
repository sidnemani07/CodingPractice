def set_zeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    row_zero = False
    col_zero = False
    for i in range(rows):
        if matrix[i][0] == 0:
            col_zero = True
            break
    
    for j in range(cols):
        if matrix[0][j] == 0:
            row_zero = True
            break
    
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    for i in range(1, rows):
        if matrix[i][0] == 0:
            for j in range(cols):
                matrix[i][j] = 0
    
    for j in range(1, cols):
        if matrix[0][j] == 0:
            for i in range(rows):
                matrix[i][j] == 0
    
    if row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    
    if col_zero:
        for i in range(rows):
            matrix[i][0] = 0

def main():
    matrix = [
        [0,2,3],
        [4,5,6],
        [7,8,9]
    ]

    set_zeros(matrix)
    print(matrix)

if __name__ == "__main__":
    main()