import hashlib
import time, os
from termcolor import colored



#define a wait time
def wait(amount):
  time.sleep(amount)
#define slow write function
def slow_Write(Text):
  TextLetters = []
  for currentLetter in Text:
    os.system('clear')
    TextLetters.append(currentLetter)
    print("".join(TextLetters))
    time.sleep(0.07)
    print(colored('error 37b <ignore None>', 'red'))
#define decoder
def decoding(decode, encode):
      return decode
      decoder = decode("")
      print(decoder)
#question generator
print(colored('which encoding would you like to use? '))
print('')
print(colored('1.)SHA-1', 'cyan'))
print(colored('2.)SHA-224', 'yellow'))
print(colored('3.)SHA-256', 'blue'))
print(colored('4.)MD5', 'magenta'))
#question input
FQ = input('input number: ')
FQ1 = ('1')
FQ2 = ('2')
FQ3 = ('3')
FQ4 = ('4')
#sha1 generator
if FQ == FQ1:
  os.system('clear')
  File = input('File Name: ')#user inputs file name
  open(File, 'wb')
  os.system('clear')

  sha1_enc =  File.encode('utf-16')#encodes with utf16
  sha1 = hashlib.sha1(sha1_enc.strip()).hexdigest()#digest sha1
  print('')
  print(slow_Write(colored('encoding in progress{}...', 'green')))
  wait(6)
  os.system('clear')
  print(slow_Write(colored('(sha1)encoding complete = ' + sha1, 'cyan')))#prints the encryption
  print('')
  print('Console clearing in 10 seconds to start the next part{}...')
  #SHA-1 decoder
  wait(10)
  os.system('clear')
  print('1.)decode')
  print('2.)end progam')
  yes1 = ('1')
  yes2 = ('2')
  decrypt1 = (input(colored('would you like to decode your sha1 encoding? ', 'cyan')))
  os.system('clear')

  #sha1 decoder
  if decrypt1 == yes1:
    decode1 = sha1_enc.decode('UTF-16', 'strict')
    wait(3)
    print(colored('activating decoders{}...', 'red'))
    wait(3)
    print(colored('decoders activated: decoding SHA1{}...', 'green'))
    wait(7)
    os.system('clear')
    wait(1)
    print(colored('decoding complete, decoding= '+ decode1, 'cyan'))
    print('')
    wait(5)
    print(colored('ALERT!', 'yellow'))
    wait(4)
    print(colored('console clearing in 25 seconds{}...', 'red'))
    wait(25)
    os.system('clear')
  
#sha224 encrypter
if FQ == FQ2:
  os.system('clear')
   #sha224 GeneratorE
  File1 = input('File Name: ')#user inputs file name to be encrypted with sha224
  os.system('clear')
  #encrypter
  File1_enc = File1.encode('utf-16')#utf16 encoding
  sha224 = hashlib.sha224(File1_enc.strip()).hexdigest()#does the encryption
  print('')
  print(slow_Write(colored('encoding in progress{}...', 'green')))#printer
  wait(6)
  os.system('clear')
  print(slow_Write(colored('(sha224)encoding complete= ' + sha224, 'yellow')))
  print('')
  wait(6)
  print(colored('Console clearing in 10 seconds to start tne next part{}...', 'red'))
  wait(10)
  #user decides if they want to decode or not
  os.system('clear')
  
  print('1.)decode')
  print('2.)end progam')
  yes1 = ('1')
  yes2 = ('2')
  decrypt224 = (input(colored('would you like to decode your sha224 encoding? ', 'yellow')))
  os.system('clear')
  #wait(10)
  #print(colored('ALERT!', 'yellow'))
  #wait(3)
  #print(colored('Console clearing in 20 seconds{}...', 'red'))
  #wait(20)
  #os.system('clear')


  if decrypt224 == yes1:
    print(slow_Write(colored('decoding in progress{}...', 'green')))
    decode224 = File1_enc.decode('utf-16', 'strict')
    wait(6)
    print(slow_Write(colored('decoding complete, decoding = ' + decode224, 'yellow')))
    wait(10)
    print('')
    print(colored('ALERT!', 'yellow'))
    wait(3)
    print(colored('Console clearing in 20 seconds{}...', 'red'))
    wait(20)
    os.system('clear')

if FQ == FQ3:
  os.system('clear')
  #sha256 generator
  File2 = input('File Name:')#sha256 encrypter
  os.system('clear')

  sha256_enc = File2.encode('utf-16')#encodes the encryption
  sha256 = hashlib.sha256(sha256_enc.strip()).hexdigest()#encrypts the input
  print(slow_Write(colored('encoding in progress{}...', 'green')))
  print('')
  wait(6)
  os.system('clear')
  print(slow_Write(colored('(sha256)encoding complete= ' + sha256, 'blue')))#printer
  print('')
  wait(4)
  print(colored('ALERT!', 'yellow'))
  wait(3)
  print(colored('console clearing in 20 seconds{}...', 'red'))
  wait(20)
  os.system('clear')

if FQ == FQ4:
  os.system('clear')
  #md5 generator 
  File3 = input('File Name: ')#file input
  os.system('clear')

  md5_enc = File3.encode('utf-16')#encoder
  md5 = hashlib.md5(md5_enc.strip()).hexdigest()#encrypter
  print('')
  print(slow_Write(colored('encoding in progress{}...', 'green')))
  wait(6)
  os.system('clear')
  print(slow_Write(colored('(MD5)encoding complete = ' + md5, 'magenta')))
  print('')
  wait(5)
  print(colored('ALERT!', 'yellow'))
  wait(3)
  print(colored('console clearing in 20 seconds{}...', 'red'))
  wait(20)
  os.system('clear')