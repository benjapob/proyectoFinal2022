import hashlib

class Encoder:

    def encode(self, string):

        result = hashlib.md5(string.encode())
        return result.hexdigest()

    def decode(self, string, claveMD5):

        if hashlib.md5(string.encode()).hexdigest() == claveMD5:
            return True
        else:
            return False

if __name__ == '__main__':
    print(Encoder().encode("666"))