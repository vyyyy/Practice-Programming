# s can be any word passed in as str
def is_palindrome(s):
    return s == s[::-1]
    
is_palindrome('racecar')  # True

is_palindrome('car')  # False
