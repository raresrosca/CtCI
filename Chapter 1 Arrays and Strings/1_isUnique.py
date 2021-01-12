def is_unique(my_string):
    """Checks to see if each character in the string is unique: O(n^2)"""
    for idx1, i in enumerate(my_string):
        for idx2, j in enumerate(my_string):
            if idx1 == idx2:
                pass
            else:
                if i == j:
                    return False
    return True

def is_unique_2(my_string):
    """Checks to see if each character in the string is unique, assuming 128 ASCII characters: O(n)"""
    if len(my_string) > 128:
        return False
    
    a = [False for _ in range(128)]
    for char in my_string:
        val = ord(char)
        if a[val]:
            return False
        a[val] = True
    return True


if __name__ == "__main__":
    test_1 = "abcdefghijklmn"
    test_2 = "qwertyqwerty"
    test_3 = "abcdefgha"
    test_4 = "12345_;]["

    print(is_unique_2(test_1))
    print(is_unique_2(test_2))
    print(is_unique_2(test_3))
    print(is_unique_2(test_4))

