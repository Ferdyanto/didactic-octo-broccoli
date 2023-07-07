from cryptography.fernet import Fernet
import pandas as pd
import math as m
import random
import operator
import csv
import os

class Random:
    def __str__(self):
        return f'Ini random'
    
    def save(self,a,dir):
        with open(dir,'wb') as b:
            b.write(a)

    def hapus(self):
        try:
            os.system('cls')
        except:
            os.system('clear')   

    def awal(self):
        print('\tKALKULATOR')

    def clear(self):
        Calc.hapus(self)
        Calc.awal(self)

    def if_zero(self,dir):
        if os.stat(dir).st_size == 0:
            c = csv.writer(open(dir, 'a'))
            c.writerow(self.first_row)       

    def wh_zero(self,dir):
        while os.path.isfile(dir) is False:
            c = csv.writer(open(dir, 'a'))
            c.writerow(self.first_row)

    def e_hist(self,dir):
        e = csv.writer(open(dir, 'w'))
        e.writerow(self.first_row)      

    def eror(self):
        print('\n\tmasukkan input yang sesuai!')

class Calc(Random):
    def __init__(self):
        self.dir_hist = 'dataset/histoop.csv' #direkotri untuk riwayat
        self.riwayat = []
        self.first_row = ['hasil','input']
    # action1
    def gen(self,a,b):
        if b == 1:
            self.n1 = a
        elif b == 2:
            self.n2 = a
        elif b==3:
            self.n3 = a
    
    def oper(self,a):
        k,l = self.n1,self.n2
        if a==1:
            b = k+l
            c = '+'
        elif a==2:
            b = k-l
            c = '-'
        elif a==3:
            b = k*l
            c = '*'
        elif a==4:
            b = k/l
            c = '/'
        elif a==5:
            b = k**l
            c = '**'
        elif a==6:
            b = k%l
            c = '%'
        elif a==7:
            b = k//l
            c = '//'
        else:
            Calc.eror(self)
            Calc.inp(self,3)
        self.hasil = b
        self.o = c

    def inp(self,b):
        a = None
        while a is None:
            try:
                if b == 1:
                    a = int(input('\n\ta = '))
                elif b == 2:
                    a = int(input('\tb = '))
                elif b == 3:
                    a = int(input('\toperasi : '))
            except:
                Calc.eror(self)
                a = None
        Calc.gen(self,a,b)

    def main1(self):
        Calc.clear(self)
        print('Operasi yang tersedia saat ini:\n1: +\n2: -\n3: *\n4: /\n5: **\n6: %\n7: //')
        Calc.inp(self,1)
        Calc.inp(self,2)
        Calc.inp(self,3)
        Calc.oper(self,self.n3)
        print('\n\ta%sb ='%self.o,self.hasil)
        self.inpt = ''.join([str(self.n1),self.o,str(self.n2)])
        del self.n1,self.n2,self.n3
        self.riwayat.append([self.hasil,self.inpt])
    # action2
    def save(self,directory):
        with open(directory,'a') as dir:
            Calc.wh_zero(self,directory)
            c = csv.writer(dir)
            Calc.if_zero(self,directory)
            for k in self.riwayat:
                c.writerow(k)
            self.riwayat.clear()
            print('\nriwayat disimpan di csv')

    def show(self):
        Calc.wh_zero(self,self.dir_hist)
        Calc.if_zero(self,self.dir_hist)
        self.histframe = pd.read_csv(self.dir_hist)
        print('\nriwayat sementara :\n')
        for i in self.riwayat:
            print(i)
        print('\nriwayat eksternal :\n',self.histframe)

    def res(self,res):
        if res == 11:
            Calc.hapus(self)
            self.riwayat.clear()
            Calc.e_hist(self,self.dir_hist)
            print('history telah direset')
        elif res == 1:
            Calc.hapus(self)
            self.riwayat.clear()
            print('history sementara telah dihapus')
        elif res == 2:
            Calc.hapus(self)
            Calc.save(self,self.dir_hist)
        else:
            Calc.clear(self)

    def main2(self):
        Calc.hapus(self)
        Calc.show(self)
        self.main2act = int(input('\n1 reset\t\t11 reset total\n2 simpan\t0 kembali\n'))
        Calc.res(self,self.main2act)
    # action3
    def filter(self,n):
        a = [i for i in n]
        for i in range(len(a)):
            if a[i] == '^':
                a.remove(a[i])
                a.insert(i,'**')
            elif a[i] == '×' or a[i] =='x':
                a.remove(a[i])
                a.insert(i,'*')
            elif a[i] == '%':
                a.remove(a[i])
                a.insert(i,'/100')
        return ''.join(a)

    def main3(self):
        Calc.clear(self)
        n = None
        def sin(x):
            return m.sin(x)
        while n==None:
            try:
                n = input('\nmasukkan input\n\n\t')
                self.inpt = Calc.filter(self,n)
                self.hasil = eval(self.inpt)
            except:
                Calc.clear(self)
                Calc.eror(self)
                n = None
        print('\t=',self.hasil)
        self.riwayat.append([self.hasil,self.inpt])
    # ui
    def mainloop(self):
        Calc.awal(self)
        while True:
            try:
                action = int(input('\n0 keluar\t1 kalkulator\n2 history\t3 kalkultor lain\n'))
                if action == 0:
                    Calc.clear(self)
                    print('\nTerima kasih sudah mampir:D')
                    break
                elif action == 1:
                    Calc.main1(self)
                elif action == 2:
                    Calc.main2(self)
                elif action == 3:
                    Calc.main3(self)
                else:
                    Calc.clear(self)
                    Calc.eror(self)
            except:
                Calc.clear(self)
                Calc.eror(self)

class Card(Random):
    def __init__(self):
        self.SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
        self.RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
        self.NCARDS = 8
        self.score = 50
        self.startDeckList =[]
        for suit in self.SUIT_TUPLE:
            for thisValue, rank in enumerate(self.RANK_TUPLE):
                self.cardDict = {'rank':rank, 'suit':suit, 'value':thisValue +1}
                self.startDeckList.append(self.cardDict)

    def getCard(self, deckListIn):
        thisCard = deckListIn.pop()
        return thisCard
    
    def shuffle(self, deckListIn):
        deckListOut = deckListIn.copy()
        random.shuffle(deckListOut)
        return deckListOut
    
    def getDict(self,b,status):
        cardDict = Card.getCard(self,b)
        cardR = cardDict['rank']
        cardS = cardDict['suit']
        cardV = cardDict['value']
        li = [cardR,cardS,cardV]
        print(f'{status} card is', li[0],'of', li[1])
        return li

    def compare(self,a,b,c):
        ops = {'>': operator.gt,
           '<': operator.lt,
           '>=': operator.ge,
           '<=': operator.le,
           '==': operator.eq}
        truth = ops[c](a,b)
        if truth is True:
            print('Correct')
            self.score += 20
        else:
            print('Wrong')
            self.score -= 15

    def main1(self):
        print('Welcome to Higher or Lower.\nYou have to choose whether the next card to be shown will be higher or lower than the current card.\nGetting it right adds 20 points; get it wrong and you lose 15 points.\nYou have 50 points to start.\n')
        while True:
            gameli = Card.shuffle(self,self.startDeckList)
            self.current = Card.getDict(self,gameli,status='Starting')
            for cardnum in range(self.NCARDS):
                answer = input('higher or lower?(h/l)\n').casefold()
                self.next = Card.getDict(self,gameli,status='Next')
                if answer == 'h':
                    Card.compare(self,self.current[2],self.next[2],'>')
                elif answer == 'l':
                    Card.compare(self,self.current[2],self.next[2],'<')
            print('Your score is:',self.score)
            self.current[0] = self.next[0]
            self.current[1] = self.next[1]
            goAgain = input('Play again?(ENTER/q)\n')
            if goAgain == 'q':
                print('Thanks for playing:D')
                break

class Gen(Random):
    def __init__(self):
        self.dir_key = ''
        self.dir_token = ''
        self.dir_token2 = 'output.txt'

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
                    self.dir_token = input('\nMasukkan nama file token:\n')+'.txt'
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
                    self.token = input('\nMasukkan token\n').encode()
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
                Gen.hapus(self)
            except:
                print('masukkan input yang benar')
                out = input('keluar?(q for quit)')
                if out.casefold() == 'q':
                    Gen.hapus(self)
                    break
                pass
