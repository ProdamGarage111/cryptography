alpha = int(input())
beta = int(input())
encrypted_message = input()
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
decrypted_message = ''
addition = 0
for i in range(alpha):
    decrypted_message = ''
    for element in encrypted_message:
        if element in alphabet:
            encrypted_letter = element
            encrypted_letter_index = alphabet.index(encrypted_letter) + 1 + addition
            decrypted_letter_index = ((encrypted_letter_index - beta) // alpha)%26
            decrypted_letter = alphabet[decrypted_letter_index - 1]
            decrypted_message = decrypted_message + decrypted_letter
        else:
            decrypted_message = decrypted_message + element 
    print(decrypted_message)
    addition = addition +26
