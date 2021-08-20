#extended eucledian for rsa has linear running time complextiy
def euc_gcd(a,b):
    # gcd(0,b) =b and a*x+b*y=b
    #x=0 y=1
    #base case
    if a==0: 
        return b,0,1
    
    gcd, x1, y1 = euc_gcd(b%a,a)
    
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x,y

print(euc_gcd(3,56))   
