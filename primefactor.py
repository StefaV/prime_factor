from tqdm import tqdm
import sys, os

#n = int(sys.argv[1])
n = 801373284

factor_list = []
prime_factors = []
flush = []

def factors(n):
    for i in tqdm (range((n-1),1,-1), desc = "Computing factors", ascii = False):
        if n % i == 0:
            factor_list.append(i)

    #Ostavljeno zbog buduće nadogradnje
    #print(factor_list)   
    os.system("clear")
    
    for i in tqdm (range(len(factor_list)), desc = "Computing primes", ascii = False):
        for j in tqdm(range(2,factor_list[i]), desc = "Factor #"+ str(i+1), ascii = False):
            if factor_list[i] % j == 0:
                flush.append(j)
        if len(flush) > 0:
            flush.clear()
        else:
            prime_factors.append(factor_list[i])
            flush.clear()  
        os.system("clear") 
    print(prime_factors)            

os.system("clear")
factors(n)