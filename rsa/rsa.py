import math
import random

def encrypt(pubK,n) :
    M = int(input("Enter plaintext"))
    C = (pow(M , pubK))
    C = math.fmod(C,n)
    return C


p = int(input("enter first prime number(p) : "))
q = int(input("\nenter second prime number (q) : "))
n = p*q
totient = (p -1)*(q-1)
arr = []
x = range(1,totient)
for e in x :
    if(math.gcd(e,n)) ==1 :
        arr.append(e)
pubK = int(random.choice(arr))
print("Your public key : ")
print(pubK)
print("\n")
C = encrypt(pubK,n)
print('Encrypted message : ' )
print(C)