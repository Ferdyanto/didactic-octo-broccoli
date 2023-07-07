from cryptography.fernet import Fernet

class Gen:

    def __init__(self):
        self.dir_key = ''
        self.dir_token = ''
        self.dir_token2 = 'output.txt'

    def save(self,a,dir):
        with open(dir,'wb') as b:
            b.write(a)

    def get(self):
        try:
            with open(self.dir_token,'r') as file:
                self.token = file.read().encode()
            return self.token
        except:
            with open(self.dir_token,'rb') as file:
                self.token = file.read()
            return self.token
        
    def loadkey(self):
        with open(self.dir_key,'rb') as file:
            self.key = file.read()
        return self.key

    def writekey(self):
        self.key = Fernet.generate_key()
        Gen.save(self,self.key,self.dir_key)
        return self.key
        
    def enkrip(self,key,token):
        f = Fernet(key)
        t_enkrip = f.encrypt(token)
        Gen.save(self,t_enkrip,self.dir_token2)
        print('hasil enskripsi:\n'+t_enkrip.decode())

    def dekrip(self,key,token):
        f = Fernet(key)
        t_dekrip = f.decrypt(token)
        Gen.save(self,t_dekrip,self.dir_token2)
        print('hasil dekripsi:\n'+t_dekrip.decode())

    def fast(self):
        self.token = Gen.get(self)
        self.key = Gen.loadkey(self)

    def main(self):
        while True:
            try:
                process = input('token melalui file?(y/n)')
                if process.casefold() == 'y':
                    self.dir_token = input('Masukkan nama file token:\n')+'.txt'
                    self.dir_key = input('Masukkan key\n')+'.key'
                    action = input('Enkripsi atau Dekripsi?(e/d)\n')
                    if action == 'e':
                        Gen.fast(self)
                        Gen.enkrip(self,self.key,self.token)
                    elif action == 'd':
                        Gen.fast(self)
                        Gen.dekrip(self,self.key,self.token)
                    else:
                        print('masukkan input yang benar')

                elif process.casefold() == 'n':
                    self.token = input('Masukkan token\n').encode()
                    self.dir_key = input('Masukkan key\n')+'.key'
                    self.key = Gen.loadkey(self)
                    action = input('Enkripsi atau Dekripsi?(e/d)')
                    if action == 'e':
                        Gen.enkrip(self,self.key,self.token)
                    elif action == 'd':
                        Gen.dekrip(self,self.key,self.token)
                    else:
                        print('masukkan input yang benar')
                out = input('\nkeluar?(q for quit)')
                if out.casefold() == 'q':
                    break
            except:
                print('masukkan input yang benar')
                out = input('keluar?(q for quit)')
                if out.casefold() == 'q':
                    break
                pass


# code = Gen('token.txt','key.key')
# token = b'gAAAAABkp7dNyjeSQjhbRwOo1WrIKiNoK6T6TGnBbJtrYdYMjo_RGJ3pmAmeNlN_RvuDrv-TXKX2UXLUGddFTJOd2uhkxuLE0eV4HhOiqdzGQ0uuJWzKw-0='
# key = code.loadkey()
# code.dekrip(key,token)

cod = Gen()
cod.main()