#!/usr/bin/env python
import base64
import os
def xor(data, key):
	return "".join(map(lambda (x,y): chr(ord(x) ^ ord(y)), zip(data, key*(len(data)/len(key)+1))))

keylen = 16

def generate_key():
	return os.urandom(keylen)

def encrypt(data, key):
	return base64.b64encode(xor(data, key))

def decrypt(data, key):
	return xor(base64.b64decode(data), key)

enc_msg1="XOvjumbdDj+Ny3Dz/dicO2bs/ukv3RsjjN52+Kmdz2hno8PpNdUFKN7DY7apxoZ4baPvpyXCEjyKz3O2vN+LO3jv66Aong=="
dec_msg1 = base64.b64decode(enc_msg1)
print dec_msg1
f_msg1 = open('msg1.txt', 'w')
f_msg1.write(dec_msg1)

enc_msg2="Ruz96TLYDmyXx2f5r8WOdXyj56w1wworm4pg/6nZz29g5qqvKtEMdt6Icfq81pR4ae3VsCnFNC6bxn7zq9SwY2fx1bk03x0lms9kya3UnX1t4P6WNdUIOYzDY+/izM01"
dec_msg2 = base64.b64decode(enc_msg2)
print dec_msg2
f_msg2 = open('msg2.txt', 'w')
f_msg2.write(dec_msg2)

enc_msg3="QOb4rGbZGGyKwn7kuZGCfnvw664jnEs4kYp0+bPXmmhto+W8NJAEPJHEcvipnc95ffeqoSOQCC2QjWO2r9SOfyj34qA1kAYpjdl28biRjnVx9OuwaA=="
dec_msg3 = base64.b64decode(enc_msg3)
print dec_msg3
f_msg3 = open('msg3.txt', 'w')
f_msg3.write(dec_msg3)

f_msg = open('msg.txt', 'w')
f_msg.write(dec_msg1 + dec_msg2 + dec_msg3)
