import random


class RSAKeyGen:
    def __init__(self):
        self.p, self.q, self.mod, self.fi, self.e, self.d = self.generate()

        with open("public_key", "w+", encoding="utf-8") as f:
            f.write(str(self.mod) + "," + str(self.e))

        with open("private_key", "w+", encoding="utf-8") as f:
            f.write(str(self.mod) + "," + str(self.d) + "," + str(self.p) + "," + str(self.q))

        print(f'p - {self.p}\nq - {self.q}\nPUBLIC_KEY (mod, e) - {self.mod}, {self.e}\nPRIVATE_KEY (mod, d) - {self.mod}, {self.d}')

    @staticmethod
    def gen_512() -> int:
        a = []
        for i in range(512):
            a.append(random.choice('01'))
        a[-1] = '1'
        a[1] = '1'
        return int((''.join(a)), 2)

    @staticmethod
    def isPrime(n: int) -> bool:
        if n < 5 and n in [1, 2, 3, 5]: return True
        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(100):
            a = random.randint(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def get_prime(self) -> int:
        while True:
            a = self.gen_512()
            if self.isPrime(a):
                return a

    @staticmethod
    def Euler(p, q) -> int:
        return (p - 1) * (q - 1)

    def generate_e(self, el) -> int:
        for i in range(2, el):

            if self.isPrime(i) and el % i != 0:
                return i

    def bezout_recursive(self, a, b):
        if not b: return 1, 0, a
        y, x, g = self.bezout_recursive(b, a % b)
        return x, y - (a // b) * x, g

    def generate(self):
        while True:
            p = self.get_prime()
            q = self.get_prime()
            mod = p * q
            fi = self.Euler(p, q)
            e = self.generate_e(fi)
            d = self.bezout_recursive(fi, e)[1]
            if d > 0:
                return p, q, mod, fi, e, d


if __name__ == '__main__':
    RSAKeyGen()
