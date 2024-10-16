def OddNumberCounter(number):
    total_odd = []
    for i in range (0, number):
        if i % 2 != 0:
            total_odd.append(i)
    return len(total_odd)

user_input = int(input('Enter a number : '))

print(OddNumberCounter(user_input))