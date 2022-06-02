class RSAEncode:
    def __init__(self, text: str):
        self.__text = ''.join([self.de_bi(ord(i)) for i in text])

        self.encode()

    @staticmethod
    def de_bi(num: int or str) -> str:
        binary = []
        while True:
            match num % 2:
                case 0:
                    num = num // 2; binary.append('0')
                case 1:
                    num = num // 2; binary.append('1')

            if num == 1: binary.append('1'); break

        binary.reverse()

        binary = ''.join(binary)
        if len(binary) % 8 != 0:
            for i in range(8 - len(binary) % 8):
                binary = '0' + binary

        return binary

    def encode(self):
        if len(self.__text) > 128:
            self.__text = list(self.__text)
            text = [self.__text[i:i + 128] for i in range(0, len(self.__text), 128)]

            if len(self.__text[-1]) < 128:
                tmp = self.de_bi((128 - len(self.__text[-1])) / 8)
                for i in range(int((128 - len(self.__text[-1])) / 8)):
                    self.__text[-1].append(tmp)

            for i in range(len(text)):
                self.__text[i] = int(''.join(text[i]), 2)

        with open('public_key', 'r', encoding='utf-8') as file:
            for line in file:
                line = [int(i) for i in line.split(',')]

                if isinstance(self.__text, list):
                    for i in range(len(self.__text)): self.__text[i] = (self.__text[i] ** line[1]) % line[0]
                else:
                    self.__text = (int(self.__text, 2) ** line[1]) % line[0]
                break

        with open('encoding_string.txt', 'w', encoding='utf-8') as file2:

            if type(self.__text) == list:
                for i in self.__text: file2.write(str(i) + '|')
            else:
                file2.write(str(self.__text))


if __name__ == '__main__':
    RSAEncode('text for test')
