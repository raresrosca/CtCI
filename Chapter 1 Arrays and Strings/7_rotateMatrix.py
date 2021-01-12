# Rotating in place only makes sense if it is a square matrix. We will assume CW rotation.
# Implement two methods, one for out-of-place rotation without shape constraints
# and one for in-place rotation of a square matrix. The matrix will be a list of lists.

from pandas import *

def rotate_out(m):
    """Rotates and returns a matrix out-of-place"""
    new_m = []
    for i in range(len(m[0])):
        row = []
        for j in range(len(m)):
            row.append(m[j][i])
        new_m.append(row)
    return new_m 


def rotate_in(m):
    """Rotates and returns a square matrix in-place"""
    if len(m) != len(m[0]):
        return None

    for i in range(len(m)-1):
        for j in range(1, len(m[0])):
            keep = m[i][j]
            m[i][j] = m[j][i]
            m[j][i] = keep
    
    return m

if __name__ == "__main__":
    test_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    test_2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    test_1_out = rotate_out(test_1)
    test_2_out = rotate_out(test_2)

    test_1_in = rotate_in(test_1)
    test_2_in = rotate_in(test_2)

    print("Original matrices: ")
    print(DataFrame(test_1))
    print(DataFrame(test_2))

    print("Out-place-rotation matrices: ")
    print(DataFrame(test_1_out))
    print(DataFrame(test_2_out))

    print("In-place-rotation matrices: ")
    print(DataFrame(test_1_in))
    #print(DataFrame(test_2_in))


