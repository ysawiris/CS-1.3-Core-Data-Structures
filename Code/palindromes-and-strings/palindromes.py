#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text, 0, len(text) - 1)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    left = 0 
    right = len(text) - 1

    while left < right: 
        
        #check if they do not match 
        if text[left].upper() != text[right].upper():
            return False 
        
        #now that they match, lets move to the next indexes 
        #and check if they match 
        left += 1
        right -= 1
    #now the while loop is done 
    #and has not return false, means that is a palindrome 
    return True 
        
    


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests
    if left == None:
        left = 0 
    
    if right == None:
        right = len(text) - 1

    #this checks if we have check every char in text 
    if left >= right:
        return True
    
    #base cases
    #check is the value is alphabet and not char or symbol
    if text[left].isalpha() is not True:
        return is_palindrome_recursive(text, left + 1, right)
    
    if text[right].isalpha() is not True:
        return is_palindrome_recursive(text, left, right - 1)

    #checks if the chars are a mismatch
    if text[left].upper() != text[right].upper():
        return False 
    
    #call the function within itself 
    #make sure the left index is less then the right index 
    if left < right: 
        return is_palindrome_recursive(text, left + 1, right - 1)
    
    return True 

    


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
