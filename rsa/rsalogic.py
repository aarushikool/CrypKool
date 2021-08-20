import random
from math import sqrt
from math import floor

start = 1e3
end = 1e5

def is_prime(number):
    if number<2:
        return False
    if number ==2:
        return True
    if number%2 ==0:
        return False
    for i in range(3, floor(sqrt(number))):
        if number %i ==0:
            return False
    
    return True

def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a

def modular_inverse(a,b):
    if a==0:
        return b,0,1
    div, x1, y1 = modular_inverse(b%a, a)
    x = y1 - (b//a) * x1
    y = x1

    return div, x,y

def generate_large_prime(s=start,e=end):
    number = random.randint(s,e)
    while not is_prime(number):
        num=random.randint(s,e)
    return number

def rsa_key_generator():
    p=generate_large_prime()
    q=generate_large_prime()
    n= p*q
    phi= (p-1)*(q-1)

    #e and phi coprimes check
    while gcd(e,phi) != 1:
        e= random.randrange(1,phi)
    
    d= modular_inverse(e,phi)[1]

    return (d,n), (e,n)
