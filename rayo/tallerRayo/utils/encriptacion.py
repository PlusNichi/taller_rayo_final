from django.core.signing import Signer
from django.conf import settings

from cryptography.fernet import Fernet
import base64

class Encriptacion:
    def encryptsign(txt):
        signer = Signer(settings.ENCRYPT_KEY)
        return signer.sign(txt)

    def decryptsign(txt):
        signer = Signer(settings.ENCRYPT_KEY)
        return signer.unsign(txt)
    
    def encrypt(txt):
        try:
            # convert integer etc to string first
            txt = str(txt)
            # get the key from settings
            cipher_suite = Fernet(settings.ENCRYPT_KEY)  # key should be byte
            # #input should be byte, so convert the text to byte
            encrypted_text = cipher_suite.encrypt(txt.encode("ascii"))
            # encode to urlsafe base64 format
            encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
            return encrypted_text
        except Exception as e:
            return None

    def decrypt(txt):
        try:
            # base64 decode
            txt = base64.urlsafe_b64decode(txt)
            cipher_suite = Fernet(settings.ENCRYPT_KEY)
            decoded_text = cipher_suite.decrypt(txt).decode("ascii")
            return decoded_text
        except Exception as e:
            return None