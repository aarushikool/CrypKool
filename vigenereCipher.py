#string alphabet is declared here to convert letters into numerical values
#ALPHABET[0] is a blank space

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def vigenere_encrypt(plain_text, key):
    plain_text=plain_text.upper()
    key=key.upper()

    cipher_text =''
    key_index=0

    for character in plain_text:
        index =(ALPHABET.find(character)+ALPHABET.find(key[key_index])) % len(ALPHABET)
        cipher_text += ALPHABET[index]
        key_index +=1

        if key_index==len(key):
            key_index=0
    
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    cipher_text=cipher_text.upper()
    key=key.upper()

    plain_text=''
    key_index=0
    for character in cipher_text:
        index =(ALPHABET.find(character)-ALPHABET.find(key[key_index])) % len(ALPHABET)
        plain_text += ALPHABET[index]
        key_index +=1

        if key_index==len(key):
            key_index=0
    return plain_text

text = 'I am a secret message dont reveal me'
cipher= 'LRZBTPCJCSKTWRKULGDYCPXCQKYGYJHSJPFT'
print(vigenere_encrypt(text,'crypto'))
print(vigenere_decrypt(cipher, 'crypto'))