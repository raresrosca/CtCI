def insert_in_list(s, idx, symbol):
    return s[:idx] + symbol + s[idx+1:]

def replace_spaces(s):
    for i in range(len(s)):
        if s[i] == " ":
            s = insert_in_list(s, i, "%20") #lists do have insert, but strings do not, so implement one
            i += 3
    return s

if __name__ == "__main__":
    test = "Mr John Smith   "
    test = replace_spaces(test)
    print(test)