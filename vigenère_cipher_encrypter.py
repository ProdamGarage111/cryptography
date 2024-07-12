key = input()
message = input()
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
encypted_message = ''
num_key = []
num_index = 0
for element in key:
    num_key.append(alphabet.index(element)+1)
for element in message:
    if element in alphabet:
        letter = element
        letter_index = alphabet.index(letter) + 1
        encypted_letter_index =(letter_index + num_key[num_index])%26
        num_index = num_index+1
        if num_index == len(key):
            num_index = 0
    else:
        encypted_message = encypted_message + element
encypted_letter = alphabet[encypted_letter_index - 1]
encypted_message = encypted_message + encypted_letter
print(encypted_message)
