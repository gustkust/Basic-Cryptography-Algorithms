import string


by_freq = 'OIHSRDLCUMWFGYPBVKJQZ,'

letters = dict.fromkeys(string.ascii_uppercase, 0)
letters['1'] = 0
letters['2'] = 0
letters['3'] = 0

with open('code.txt', 'r') as file:
    text = file.read().replace('\n', '')

with open('3words.txt', 'r') as file:
    words = file.read().replace('\n', '')

for char in text.upper():
    if (97 <= ord(char) <= 122) or (65 <= ord(char) <= 90):
        letters[char] += 1
    if char == ' ':
        letters['1'] += 1
    if char == '.':
        letters['2'] += 1
    if char == ',':
        letters['3'] += 1

for i in letters.keys():
    print(i, letters[i])

counter_letters = dict.fromkeys(string.ascii_uppercase, '')
counter_letters['1'] = ''
counter_letters['2'] = ''
counter_letters['3'] = ''

lbf = len(by_freq)
for i in range(lbf):
    counter_letters[max(letters, key=letters.get)] = by_freq[0]
    letters[max(letters, key=letters.get)] = -1
    by_freq = by_freq[1:]


counter_letters['K'], counter_letters['H'] = 'H', counter_letters['K']
counter_letters['H'], counter_letters['E'] = 'E', counter_letters['H']

# for k in counter_letters.keys():
#     print(k, counter_letters[k])
res = ''
# SPACJA = SPACJA
# W = T
# K = H
# H = E
# D = A
# A = X
# V = N
# KROPKA = KROPKA
for char in text:
    if char == ' ':
        res += ' '
    elif char == 'W':
        res += 'T'
    elif char == 'H':
        res += 'E'
    elif char == 'A':
        res += 'X'
    elif char == 'V':
        res += 'N'
    elif char == '.':
        res += '.'
    elif char == ' ':
        res += counter_letters['1']
    elif char == '.':
        res += counter_letters['2']
    elif char == ',':
        res += counter_letters['3']
    elif (97 <= ord(char) <= 122) or (65 <= ord(char) <= 90):
        res += counter_letters[char]

print(text)
# print(res)


# H W D i SPACJA najczesciej w tekscie
# E T A i SPACJA najczesciej normalnie

guesses = {
    'A': 'X',
    'W': 'T',  # 9
    'K': 'H',  # 8
    'H': 'E',  # 9
    'R': 'O',  # 7
    'Q': 'N',  # 8
    'D': 'A',  # 9
    'O': 'L',  # 5
    'U': 'R',  # 8
    'V': 'S',
    'G': 'D',
    'L': 'I',
    'F': 'C',
    'E': 'B',
    'I': 'F',  # 7
    'S': 'P',
    'B': 'Y',
    'N': 'K',
    'X': 'U',
    'J': 'G',
    'Y': 'V',
    'Z': 'W',
    'T': 'Q',
    'P': 'M'
}

text = list(text)
for i in range(len(text)):
    if text[i] in guesses.keys():
        text[i] = guesses[text[i]]
text = ''.join(text)


print(text)

# for i in text.split():
#     if len(i) > 5:
#         print(i[-3], i[-2], i[-1])
