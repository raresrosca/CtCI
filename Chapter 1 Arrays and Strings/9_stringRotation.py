import unittest

def is_rotation(s1, s2):
    """Return True if s2 is a rotation of s1, False otherwise"""
    for i, c in enumerate(s2):
        if c == s1[0]:
            if s2[i:]+s2[:i] == s1:
                return True
    return False

def is_rotation_2(s1, s2):
    """Return True if s2 is a rotation of s1, False otherwise. Uses the 'in' operator."""
    if len(s1) == len(s2) != 0 and s2 in s1+s1:
        return True
    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = is_rotation_2(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
