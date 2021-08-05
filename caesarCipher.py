#string alphabet is declared here to convert letters into numerical values
#ALPHABET[0] is a blank space

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#private key
KEY= 5
#encryption 
def caesar_encrypt(plain_text):
    cipher_text = ''
    #the algorithm is case insensitive
    plain_text= plain_text.upper()
    for c in plain_text:
    #index of each letter in plaintext can be found with:
     index = ALPHABET.find(c)
    #Caesar cipher is a shift cipher, 
    #meaning each letter in plaintext is shifted by a specific number (the KEY) for an instance.
    #This is done by calculating the index of the letters in the english alphabet
    #Mod (%) function is used so that the shifted index is in the range 0-number_of_letters_in_alphabet
     index= (index + KEY) % len(ALPHABET)
     cipher_text += ALPHABET[index]

    return cipher_text

#decryption
def caesar_decrypt(cipher_text):
    plain_text = ''

    for c in cipher_text:
        index = ALPHABET.find(c)
        index= (index - KEY) % len(ALPHABET)
        plain_text += ALPHABET[index]
    
    return plain_text

encrypted = caesar_encrypt('This is CrypKool')
print(encrypted)
decrypted= caesar_decrypt('YMNXENXEHWCUPTTQ')
print(decrypted)