# Checks Palindrome of a string
def is_palindrome(s):
    string = str(s)        

    left = 0
    right = len(string) - 1

    while left < right:
        if(string[left] != string[right]):
            return False
        right = right - 1
        left = left + 1

    return True
    # return string == string[::-1] # string slicing 

# counts the number of vowles from given string
def count_vowel(s):
    vowel = ["a","e","i","o","u"]
    found_vowel = list(filter(lambda x: x.lower() in vowel , s))
    return len(found_vowel)

def reverse_words(s):
    string = str(s)
    return string[::-1]

    
VERSION = "1.0"