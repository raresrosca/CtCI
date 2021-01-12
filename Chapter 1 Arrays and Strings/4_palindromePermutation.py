
def is_palindrome_permutation(str_1):
    "Checks if the given string is a permutation of a palindrome and returns True or False respectively; O(n)"
    str_1 = str_1.lower() #transform to lowercase
    str_1 = str_1.replace(" ", "") #remove all spaces
    my_dictionary = {}
    for i in str_1:
        if i in my_dictionary:
            my_dictionary.pop(i)
        else:
            my_dictionary[i] = 1

    if len(my_dictionary.values()) == 1 or len(my_dictionary.values()) == 0:
        return True
    return False

 


if __name__ == "__main__":
    test_1 = "Tact Coa"
    test_2 = "1234123"
    test_3 = "asdfgh"
    test_4 = 'Able was I ere I saw Elba'
    test_5 = 'no x in nixon'

    print(is_palindrome_permutation(test_1))
    print(is_palindrome_permutation(test_2))
    print(is_palindrome_permutation(test_3))
    print(is_palindrome_permutation(test_4))
    print(is_palindrome_permutation(test_5))