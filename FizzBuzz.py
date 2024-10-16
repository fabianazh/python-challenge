# Print "Fizz" if the number is divisible by 3.
# Print "Buzz" if it is divisible by 5.
# Print "FizzBuzz" if it is divisible by 3 and 5.

def FizzBuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
    
user_input = int(input('Enter a number : '))

print(FizzBuzz(user_input))