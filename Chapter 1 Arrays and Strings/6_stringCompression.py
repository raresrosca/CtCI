
def compress_string(str_1):
    """Compresses a string or returns original string if the compressed value is larger"""
    str_2 = ""
    idx = 0
    while idx < len(str_1):
        i = 1
        try:
            while str_1[idx] == str_1[idx+i]:
                i += 1
        except IndexError:
            pass
        str_2 += str_1[idx]
        str_2 += f"{i}"
        idx += i
    
    if len(str_2) < len(str_1):
        return str_2
    else:
        return str_1


if __name__ == "__main__":
    test_1 = 'aabcccccaaa'
    test_2 = 'qwertyuiop'
    test_3 = 'qqqerrrtmmmzz'
    print(compress_string(test_1))
    print(compress_string(test_2))
    print(compress_string(test_3))