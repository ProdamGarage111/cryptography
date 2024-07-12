alpha = int(input())
beta = int(input())
message = input()
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
encypted_message = ''
for element in message:
    if element in alphabet:
        letter = element
        letter_index = alphabet.index(letter) + 1
        encypted_letter_index = (letter_index * alpha + beta)%26
        encypted_letter = alphabet[encypted_letter_index - 1]
        encypted_message = encypted_message + encypted_letter
    else:
        encypted_message = encypted_message + element

print(encypted_message)
        