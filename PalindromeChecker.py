# Check if text is a Palindrome

def PalindromeChecker(text):
    isPalindrome = True if text[::-1] == text else False
    return isPalindrome
    
user_input = input('Enter a text : ')

print(PalindromeChecker(user_input))