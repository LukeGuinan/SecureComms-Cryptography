#CODE TAKEN FROM - https://asecuritysite.com/homomorphic/hom_password 

import sys
from random import randint
import bitarray

def to_bin(string):
    res = ''
    for char in string:
        tmp = bin(ord(char))[2:]
        tmp = '%08d' %int(tmp)
        res += tmp
    return res

def inv(val):
	return(val ^ 1)

#PASSWORD VALUES
B00096856='A'
LukeGuinan='B'

#PRINT VALUES
print("Luke's Password: ",B00096856, "Luke's Alt Password: ",LukeGuinan)

#CONVERT TO BINARY VALUES
bits1 = to_bin(B00096856)
bits2 = to_bin(LukeGuinan)

print("Bits:\t",bits1)
print("Bits:\t",bits2)

#PRINT 8 CHARACTER BINARY VALUE
c_bits1 = [0 for i in range(8)]
c_bits2 = [0 for i in range(8)]
	
p =randint(300000, 600000)*2+1

#PRINT CIPHER VALUES FOR Q & R
print("Cipher bits 1:")
print("Bit\tCipher\t\tq\t\tr")
for i in range(0,8):
	q=randint(50000000, 90000000)
	r=randint(1,200)
	c_bits1[i] =  q * p + 2*r +int(bits1[i])
	print(bits1[i], "\t",c_bits1[i],"\t",q,"\t",r)
	if (2*r > p/2): 
		print('Error')

print()
print("Cipher bits 2:")
print("Bit\tCipher\t\tq\t\tr")
for i in range(0,8):
	q=randint(50000000, 90000000)
	r=randint(1,200)
	c_bits2[i] =  q * p + 2*r +int(bits2[i])
	print(bits2[i], "\t",c_bits2[i],"\t",q,"\t",r)
	if (2*r > p/2): 
		print('Error')

cipher_bit7 = (  (inv(c_bits1[7]) * inv(c_bits2[7]) ) + ( c_bits1[7] * c_bits2[7] ) ) 
cipher_bit6 = (  (inv(c_bits1[6]) * inv(c_bits2[6]) ) + ( c_bits1[6] * c_bits2[6] ) ) 
cipher_bit5 = (  (inv(c_bits1[5]) * inv(c_bits2[5]) ) + ( c_bits1[5] * c_bits2[5] ) ) 

print()	
print("p value:\t",p)


print("\nCipher result:")
print(cipher_bit5, cipher_bit6, cipher_bit7)

#decrypt
result7 = (cipher_bit7 % p) % 2
result6 = (cipher_bit6 % p) % 2
result5 = (cipher_bit5 % p) % 2

#PULL RESULTS AND COMPARE THE VALUES
print("\nResults")

print(result5,result6,result7)

if ((result7==1) and (result6==1) and (result5==1)):
	print("Passwords are the same")
else:
	print("Passwords are not the same")