"""Network Threading"""
import sys
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


class AESCipher:

    def __init__(self, key: str):
        self.bs = AES.block_size
        self.key = key

    def encrypt(self, raw: str) -> str:
        raw = self._pad(raw)
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode('utf8')))

    def decrypt(self, enc: str) -> str:
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._un_pad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s: str) -> str: return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _un_pad(s: str) -> str: return s[:-ord(s[len(s) - 1:])]
