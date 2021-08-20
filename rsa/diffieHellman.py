import random as rnd
from rsalogic import generate_large_prime

def private_key_generator(n,g):
    x= rnd.randint(1,n)
    y= rnd.randint(1,n)
    k1 = pow(g,x,n)
    k2= pow(g,y,n)
    print("Sender's private key %s" %(pow(k2,x,n)))
    print("Reciever's private key %s" %(pow(k1,y,n)))

n=1199
g=131
private_key_generator(n,g)
