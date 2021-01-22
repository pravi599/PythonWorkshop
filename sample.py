

def Is_Even(n):
    if n%2==0:
        return True
    else:
        return False

    
    
    
    
    
def Is_prime(n):
    if n==1:
        return False
    cnt = 0
    for i in range(2,n):
        if n%i==0:
            cnt+=1
            break
    if cnt == 0:
        return True
    else:
        return False
Is_prime(5)    