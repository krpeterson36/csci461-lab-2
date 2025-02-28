import json

from base64 import b64encode, b64decode

from Crypto.Cipher import AES

from Crypto.Util.Padding import pad, unpad

from Crypto.Random import get_random_bytes

def encrypt():
    data = b"secret"

    key = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC)

    ct_bytes = cipher.encrypt(pad(data, AES.block_size))

    iv = b64encode(cipher.iv).decode('utf-8')

    ct = b64encode(ct_bytes).decode('utf-8')

    result = json.dumps({'iv':iv, 'ciphertext':ct})

    print(result)

    return result, key

def decrypt(json_input, key):
    try:
        b64 = json.loads(json_input)

        iv = b64decode(b64['iv'])

        ct = b64decode(b64['ciphertext'])

        cipher = AES.new(key, AES.MODE_CBC, iv)

        pt = unpad(cipher.decrypt(ct), AES.block_size)

        print("The message was: ", pt)

    except (ValueError, KeyError):

        print("Incorrect decryption")

def main():
    result, key = encrypt()
    decrypt(result, key)

if __name__ == "__main__":
    main()