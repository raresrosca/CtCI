from collections import Counter 

def is_permutation(str_1, str_2):
    """Returns True if str_2 is a permutaiton of str_1 and False otherwise O(n)"""
    my_dictionary = {}

    if len(str_1) != len(str_2):
        return False
    
    for i in str_1:
        if i in my_dictionary:
            my_dictionary[i] += 1
        else:
            my_dictionary[i] = 1
    
    for i in str_2:
        if i in my_dictionary:
            my_dictionary[i] -= 1
        else:
            return False
    
    for value in my_dictionary.values():
        if value != 0:
            return False
    
    return True

def is_permutation_2(str_1, str_2):
    """Returns True if str_2 is a permutaiton of str_1 and False otherwise O(n)"""
    if len(str_1) != len(str_2):
        return False

    counter = Counter()
    for c in str_1:
        counter[c] += 1
    for c in str_2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True




if __name__ == "__main__":
    string_1 = "abcd"
    string_2 = "bcda"
    string_3 = "aabb"
    string_4 = "bbax"

    print(is_permutation_2(string_1, string_2))
    print(is_permutation_2(string_1, string_3))
    print(is_permutation_2(string_3, string_4))

