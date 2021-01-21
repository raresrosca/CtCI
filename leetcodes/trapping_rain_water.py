from pandas import DataFrame

def matrix_from_array(arr):
    """Transforms the input array into a matrix"""
    height = max(arr)
    width = len(arr)
    mat = [[0 for i in range(width)] for j in range(height)]

    for col in range(len(arr)):
        for row in range(arr[col]):
            mat[row][col] += 1
    return mat

def count_water(mat):
    counter = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                if sum(mat[i][:j]) >= 1 and sum(mat[i][j:]) >= 1:
                    counter += 1
    return counter

def count_water_2(mat):
    counter = 0
    for i in range(len(mat)):
        temp = 0
        toggle = False
        for j in range(len(mat[0])):
            if mat[i][j] == 1 and toggle == False:
                toggle = True
            elif mat[i][j] == 1 and toggle == True:
                counter += temp
                temp = 0
            elif mat[i][j] == 0 and toggle == True:
                temp += 1
    return counter




if __name__ == "__main__":
    i1 = [0,1,0,2,1,0,1,3,2,1,2,1] #6
    i2 = [4,2,0,3,2,5] #9
    m1 = matrix_from_array(i1)
    m2 = matrix_from_array(i2)
    c1 = count_water(m1)
    c2 = count_water(m2)
    c3 = count_water_2(m1)
    c4 = count_water_2(m2)
    print(c1)
    print(c2)
    print(c3)
    print(c4)
    #print(DataFrame(m1))