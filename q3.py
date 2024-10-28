# 3.	Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation) 
  
def check_if_pangram(input_str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input_str = input_str.lower()
    for letter in alphabet:
        if letter not in input_str:
            return False
    return True 

# Example usage:
print(check_if_pangram("The quick brown fox jumps over the lazy dog"))  # Output: True
print(check_if_pangram("Hello World"))                                   # Output: False
