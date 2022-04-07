def prepare_cryptogram(cryptogram):
    for i in range(0, len(cryptogram) + 1, 2):
        if i < len(cryptogram) - 1:
            if cryptogram[i] == cryptogram[i + 1]:
                cryptogram = cryptogram[:i + 1] + "X" + cryptogram[i + 1:]

    if len(cryptogram) % 2 != 0:
        cryptogram += "X"

    return cryptogram


def create_matrix(key):
    matrix_5x5 = [[0 for i in range(5)] for j in range(5)]
    matrix_text = []

    for c in key:
        if c not in matrix_text:
            if (c == "J" or c == "I") and not "I" in matrix_text:
                matrix_text.append("I")
            elif (c == "J" or c == "I") and "I" in matrix_text:
                pass
            else:
                matrix_text.append(c)

    i_in_matrix = "I" in matrix_text

    for i in range(ord("A"), ord("Z") + 1):
        if chr(i) not in matrix_text:
            if (i == ord("I") or i == ord("J")) and not i_in_matrix:
                matrix_text.append("I")
                i_in_matrix = True
            elif (i == ord("I") or i == ord("J")) and i_in_matrix:
                pass
            else:
                matrix_text.append(chr(i))

    index = 0
    for i in range(0, 5):
        for j in range(0, 5):
            matrix_5x5[i][j] = matrix_text[index]
            index += 1

    return matrix_5x5


def encryption(key, text):
    result = []
    matrix = create_matrix(key)
    i = 0
    while i < len(text):
        old_i1, old_i2 = [0, 0], [0, 0]
        for j in range(5):
            for k in range(5):
                if matrix[j][k] == text[i]:
                    old_i1 = [j, k]
                elif matrix[j][k] == text[i + 1]:
                    old_i2 = [j, k]
        if old_i1[1] == old_i2[1]:
            new_i1 = [(old_i1[0] + 1) % 5, old_i1[1]]
            new_i2 = [(old_i2[0] + 1) % 5, old_i2[1]]
            result.append(matrix[new_i1[0]][new_i1[1]])
            result.append(matrix[new_i2[0]][new_i2[1]])
        elif old_i1[0] == old_i2[0]:
            new_i1 = [old_i1[0], (old_i1[1] + 1) % 5]
            new_i2 = [old_i2[0], (old_i2[1] + 1) % 5]
            result.append(matrix[new_i1[0]][new_i1[1]])
            result.append(matrix[new_i2[0]][new_i2[1]])
        else:
            result.append(matrix[old_i1[0]][old_i2[1]])
            result.append(matrix[old_i2[0]][old_i1[1]])
        i += 2
    return ''.join(result)


def decryption(key, result):
    text = []
    matrix = create_matrix(key)
    i = 0
    while i < len(result):
        old_i1, old_i2 = [0, 0], [0, 0]
        for j in range(5):
            for k in range(5):
                if matrix[j][k] == result[i]:
                    old_i1 = [j, k]
                elif matrix[j][k] == result[i + 1]:
                    old_i2 = [j, k]
        if old_i1[1] == old_i2[1]:
            new_i1 = [(old_i1[0] - 1) % 5, old_i1[1]]
            new_i2 = [(old_i2[0] - 1) % 5, old_i2[1]]
            text.append(matrix[new_i1[0]][new_i1[1]])
            text.append(matrix[new_i2[0]][new_i2[1]])
        elif old_i1[0] == old_i2[0]:
            new_i1 = [old_i1[0], (old_i1[1] - 1) % 5]
            new_i2 = [old_i2[0], (old_i2[1] - 1) % 5]
            text.append(matrix[new_i1[0]][new_i1[1]])
            text.append(matrix[new_i2[0]][new_i2[1]])
        else:
            text.append(matrix[old_i1[0]][old_i2[1]])
            text.append(matrix[old_i2[0]][old_i1[1]])
        i += 2
    return ''.join(text)


key = input("Key: ").replace(" ", "").upper()

text = input("Text: ")

# with open('text.txt', 'r') as file:
#     text = file.read().replace('\n', '')

tmp = ""
for char in text.upper():
    if (97 <= ord(char) <= 122) or (65 <= ord(char) <= 90):
        if char == "J":
            tmp += "I"
        else:
            tmp += char
text = prepare_cryptogram(tmp)

# print(encryption(key, text))
print(decryption(key, prepare_cryptogram(text.upper())))
