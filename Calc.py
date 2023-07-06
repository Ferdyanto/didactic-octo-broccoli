import math as m
import csv
import pandas as pd
import os

#declare varibles
dir_hist = 'hist.csv' #your directory
riwayat = []
first_row = ['hasil','input']

#define functions
def hapus():
  try:
    os.system('cls')
  except:
    os.system('clear')
    
def awal():
  print('\tKALKULATOR')

def clear():
  hapus()
  awal()

def if_zero(dir):
  if os.stat(dir).st_size==0:
    c = csv.writer(open(dir,'a'))
    c.writerow(first_row)
        
def wh_zero(dir):
  while os.path.isfile(dir) is False:
    c = csv.writer(open(dir,'a'))
    c.writerow(first_row)

def e_hist(dir):
  e = csv.writer(open(dir,'w'))
  e.writerow(first_row)
                    
def eror():
  print('\n\tmasukkan input yang sesuai!')

#Process  
awal()
while True:
  try:
    action = int(input('\n0 keluar\t1 kalkulator\n2 history\t3 kalkultor lain\n'))  
    
    if action==0:
      clear()
      print('\nTerima kasih sudah mampir:D')
      break
    
    elif action==1: 
      clear()
      print('Operasi yang tersedia saat ini:\n1: +\n2: -\n3: *\n4: /\n5: **\n6: %\n7: //')
      pass
      n1 = None
      n2 = None
      n3 = None
      while n1 is None:
        try:
          n1 = int(input('\n\ta = '))
        except:
          eror()
          n1 = None
      while n2 is None:
        try:
          n2 = int(input('\tb = '))
        except:
          eror()
          n2 = None
      while n3 is None:
        try:
          n3 = int(input('\taksi: '))
          if n3==1:
            hasil = n1+n2
            o = '+'
          elif n3==2:
            hasil = n1-n2
            o = '-'
          elif n3==3:
            hasil = n1*n2
            o = '*'
          elif n3==4:
            hasil = n1/n2
            o = '/'
          elif n3==5:
            hasil = n1**n2
            o = '**'
          elif n3==6:
            hasil = n1%n2
            o = '%'
          elif n3==7:
            hasil = n1//n2
            o = '//'
          else:
            eror()
            n3 = None
        except:
          eror()
          n3 = None
      print('\n\ta%sb ='%o,hasil)
      inp = ''.join([str(n1),o,str(n2)])
      riwayat.append([hasil,inp])
    
    elif action==2:
      hapus()
      wh_zero(dir_hist)
      if_zero(dir_hist)
      r = pd.read_csv(dir_hist)
      print('\nriwayat sementara :\n')
      for i in riwayat:
        print(i)
      print('\nriwayat eksternal :\n',r)
      res = int(input('\n1 reset\t\t11 reset total\n2 simpan\t0 kembali\n'))
      
      if res==11:
        hapus()
        riwayat.clear()
        e_hist(dir_hist)
        print('\nhistory telah direset')
      
      elif res==1:
        hapus()
        riwayat.clear()
        print('\nriwayat sementara dihapus')
      
      elif res==2:
        hapus()
        with open(dir_hist,'a') as dir:
          wh_zero(dir_hist)
          c = csv.writer(dir)
          if_zero(dir_hist)
          for k in riwayat:
            c.writerow(k)
          riwayat.clear()
          print('\nriwayat disimpan di csv')
      
      else:
        clear()
        eror()
        
    elif action==3:
      clear()
      n = None
      h = None
      def sin(x):
        return m.sin(x)
      while n==None:
        try:
          n = input('\nmasukkan input\n\n\t')
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
          n = ''.join(a)
          h = eval(n)
        except:
          eror()
          n = None
      print('\t=',h)
      riwayat.append([h,n])
        
    else:
      clear()
      eror()
  except:
    clear()
    eror()
