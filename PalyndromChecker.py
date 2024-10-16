# Check if word is a Palyndrom

def PalyndromChecker(text):
    isPalyndrom = True if text[::-1] == text else False
    return isPalyndrom
    
user_input = input('Enter a text : ')

print(PalyndromChecker(user_input))