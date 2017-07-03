class Cipher:
    """Base Cipher Class"""
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()
