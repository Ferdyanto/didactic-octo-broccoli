from cryptography.fernet import Fernet

dir_key = 'key.key'
dir_token = 'token.txt'
dir_encrypted = 'encrypted_token.txt'

def save(a,dir):
    with open(dir,'wb') as b:
        b.write(a)
        
def loadkey(dir):
     with open(dir, 'rb') as file_key:
        key = file_key.read()
     return key

def writekey(dir):
    key = Fernet.generate_key()
    save(key,dir)
    return key

def get(dir):
    with open(dir,'r') as file_token:
        token = file_token.read().encode()
    return token

#writekey(dir_key)
f = Fernet(loadkey(dir_key))

token_encrypted = f.encrypt(get('token.txt'))
save(token_encrypted,dir_encrypted)
print(token_encrypted.decode())

token_decrypted = f.decrypt(token_encrypted)
save(token_decrypted,dir_token)
#print(token_decrypted.decode())