import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
combined = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^',
            '&', '*', '(', ')', '[', ']', '{', '}', '/', '"', '+', '-', ':', ';', '<', '>', '_', '`', '~']

minimum = int(input('ENTER MINIMUM LENGTH OF PASSWORD:'))
special_char = input('ALLOWANCE OF SPECIAL CHARACTERS(Y OR N):')

if special_char == 'N':
    password = ''
    length = random.randint(minimum, minimum+6)
    for i in range(length):
        data = random.choice(letters)
        password = password + data
    print(password)
elif special_char == 'Y':
    password = ''
    length = random.randint(minimum, minimum+6)
    for i in range(length):
        data = random.choice(combined)
        password = password + data
    print(password)
else:
    print('INVALID INPUT')
