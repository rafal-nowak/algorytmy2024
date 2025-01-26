import math
import random

class RSAKeyGenerator:
    @staticmethod
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    @staticmethod
    def mod_inverse(A, M):
        if math.gcd(A, M) > 1:
            # modulo inverse does not exist
            return -1
        for X in range(1, M):
            if (((A % M) * (X % M)) % M == 1):
                return X
        return -1
    
    @staticmethod
    def generate_primes(approx_digits_num):
        min_range, max_range = 10**(approx_digits_num-1), 10**(approx_digits_num+1)
        p = random.randint(min_range, max_range)
        while not RSAKeyGenerator.is_prime(p):
            p += 1
        q = random.randint(p + 1, max_range + p)
        while not RSAKeyGenerator.is_prime(q):
            q += 1
        
        # return p, q
        # Skrypt działa tylko z małymi liczbami z powodu wykonywanej operacji potęgowania.
        # (w praktyce nie wykonuje się tej operacji, tylko używa się innych metod obliczania [a^b mod c])
        return 13, 53
    
    @staticmethod
    def generate_keys():
        # krok 1
        p, q = RSAKeyGenerator.generate_primes(approx_digits_num=2)
        print(f"p = {p}")
        print(f"q = {q}")
    
        # krok 2
        n = p*q
        print(f"n = {n}")
    
        # krok 3
        phi = (p - 1) * (q - 1)
    
        # krok 4
        e = 2
        if math.gcd(e, phi) != 1:
            e = 2
            while(e < phi):
                if (math.gcd(e, phi) == 1):
                    break
                e += 1
        
        print(f"e = {e}")
        print(f"phi = {phi}")
        
        # krok 5
        # wybieramy d, jest odwrotnością modularną liczby e
        
        d = RSAKeyGenerator.mod_inverse(e, phi)
        
        print(f"d = {d}")
        
        public_key = (n, e)
        private_key = (n, d)
        
        print(f'Public key: {public_key}')
        print(f'Private key: {private_key}')
        
        return public_key, private_key
    