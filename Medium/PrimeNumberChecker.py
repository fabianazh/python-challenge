# Check if a number is a prime number

def PrimeNumberChecker(number):
    return True if number % number == 0 else False

user_input = int(input('Enter a number : '))

print(PrimeNumberChecker(user_input))