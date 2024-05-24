from math import sqrt

def isprime(p):

# votre code ici
        
    for d in range(2, p):
        if p%d == 0:
            return False
    
    return True

def main():

    for i in range(1, 100):
        if isprime(i):
            print(i)

if __name__ == "__main__":
    main()
