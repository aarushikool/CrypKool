#string alphabet is declared here to convert letters into numerical values
#ALPHABET[0] is a blank space

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def crack_caesar(cipher_text):
    #in brute force we will try all the possble key values of the ALPHABET
    for KEY in range(len(ALPHABET)):
        # we will reintailize this to plaintext = ''
        plain_text = ''
        #caesar decryption:
        plain_text = ''
        #decrypt function
        for c in cipher_text:
          index = ALPHABET.find(c)
          index= (index - KEY) % len(ALPHABET)
          plain_text += ALPHABET[index]

        print('With key %s, the result is %s' % (KEY,plain_text))


encrypted = 'YMNXENXEFEXJHWJYERJXXFLJEYMFYERZXYEGJE JWCEXFKJ'
crack_caesar(encrypted)