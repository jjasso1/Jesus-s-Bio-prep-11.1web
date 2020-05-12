import numpy as np

# A is a 2D matrix defined as a nested tuple here
A = ((4,6),(3,8))
B = ((6,1,1),(4,-2,5),(2,8,7))

A_np = np.array(A)
B_np = np.array(B)

# find the determinant of A (check if A is nonsingular)
def determinant(matrix):
    # is matrix 1by1 ?
    if len(matrix) == 1:
        return matrix[0,0]
    else:
        split_size = len(matrix)//2
        det_result = 0
        sign = -1
        col_counter = 0
        for iter in len(matrix)%2+2:
            mat1 = matrix[:split_size, col_counter:split_size]
            mat2 = matrix[split_size:, split_size:]
            det_result = det_result + sign*determinant(mat1)*determinant(mat2)
        
        
        return  det_result


print(determinant(A_np))
print(determinant(B_np))