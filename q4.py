# Write a program that takes an integer as input and returns an integer with
# reversed digit ordering.

def reverse_integer(n):
    reversed_str = str(n)[::-1]
        reversed_int = int(reversed_str)
    return reversed_int

# Example 
num = int(input("Enter an integer: "))
result = reverse_integer(num)
print("Reversed integer:", result)
