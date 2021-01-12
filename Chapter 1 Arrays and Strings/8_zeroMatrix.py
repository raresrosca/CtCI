from pandas import *

def zero_matrix(m):
    coordinates = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                coordinates.append([i, j])
    
    for coord in coordinates:
        row = coord[0]
        col = coord[1]
        for i in range(len(m)):
            m[i][col] = 0
        for j in range(len(m[0])):
            m[row][j] = 0
    
    return m



if __name__ == "__main__":
    test_1 = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    test_2 = [[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 0]]

    test_1_new = zero_matrix(test_1)
    test_2_new = zero_matrix(test_2)

    print(DataFrame(test_1_new))
    print(DataFrame(test_2_new))