
# 2.	Write a Python function that checks whether a word or phrase is palindrome or not.  


def check_palindrome(phrase):
    cleaned_phrase = phrase.replace(" ", "").lower()
    
    reversed_phrase = cleaned_phrase[::-1]
    
    if cleaned_phrase == reversed_phrase:
        print("The phrase is a palindrome")
    else:
        print("The phrase is not a palindrome")

check_palindrome("A man a plan a canal Panama")  # Output: The phrase is a palindrome
check_palindrome("Hello")  