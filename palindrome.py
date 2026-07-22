
def is_palindrome(num):
    num_str = str(num)
    cleaned_str = num_str.replace(" ", "").lower()
    return cleaned_str == cleaned_str[::-1]


num = input("Enter a number: ")
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")