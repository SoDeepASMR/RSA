class RSADecode:
    def __init__(self):
        self.decode()

    @staticmethod
    def decode():
        with open('encoding_string.txt', 'r+', encoding='utf-8') as file:
            for line in file:
                if '|' in line:
                    line = line.split('|')
                with open('private_key', 'r+', encoding='utf-8') as file2:
                    for line2 in file2:
                        line2 = [int(i) for i in line2.split(',')]
                        if type(line) != list:
                            text = format(pow(int(line), line2[1], line2[0]), 'b')

                            if len(text) % 8 != 0:
                                for i in range(8 - len(text) % 8): text = '0' + text

                            text = ''.join([chr(int(text[i:i + 8], 2)) for i in range(0, len(text), 8)])

                        else:
                            text = [0 for i in range(len(line) - 1)]
                            for i in range(len(text)):
                                text[i] = format(pow(int(line[i]), line2[1], line2[0]), 'b')

                            for i in range(len(text)):
                                if len(text[i]) % 8 != 0:
                                    for j in range(8 - len(text[i]) % 8):
                                        text[i] = "0" + text[i]

                            text = "".join(text)

                            text = [(text[i:i + 8]) for i in range(0, len(str(text)), 8)]

                            tmp = int(text[-1], 2)
                            for i in range(tmp): text.pop()
                            for i in range(len(text)): text[i] = chr(int(text[i], 2))

                        print(''.join(text))
                break

    @staticmethod
    def ChineseTheorem(a, a1, b, b1) -> int:
        M0 = a1 * b1;
        m = b1;
        m1 = a1

        print(f'''
        r1 - {a}
        r2 - {b}
        p - {a1}
        q - {b1}
        ''')

        m = m - ((m // b) * b)
        y = None
        for i in range(1, b + 1):
            if ((m * i) - a) % b == 0:
                y = i
                break

        m1 = m1 - ((m1 // b1) * b1)
        y1 = None
        for i in range(1, b1 + 1):
            if ((m1 * i) - a1) % b1 == 0:
                y1 = i
                break

        x = M0 % ((m * y) + (m1 * y1))
        return x


if __name__ == '__main__':
    RSADecode()
