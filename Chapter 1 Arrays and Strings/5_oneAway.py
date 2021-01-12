
def one_away(str_1, str_2):
    """Checks to see if str_1 and str_2 are one edit (insert, replace, remove) away from each other; O(s1+s2)"""
    if str_1 == str_2:
        return True
    
    if abs(len(str_1)-len(str_2)) >= 2:
        return False

    my_dictionary = {}

    for c in str_1:
        if c in my_dictionary:
            my_dictionary[c] += 1
        else:
            my_dictionary[c] = 1
    
    for c in str_2:
        if c in my_dictionary:
            my_dictionary[c] -= 1
        else:
            my_dictionary[c] = 1

    if 0 <= sum(my_dictionary.values()) <= 2:
        return True
    else:
        return False
    


if __name__ == "__main__":
    test_11 = "pale"
    test_12 = "pal"
    test_21 = "My name is Rares"
    test_22 = "My name is John"
    test_31 = "I am a man"
    test_32 = "I km a man"

    print(one_away(test_11, test_12))
    print(one_away(test_21, test_22))
    print(one_away(test_31, test_32))