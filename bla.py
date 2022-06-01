from operator import not_
from unicodedata import decimal


flag="hello"
key=[0,0,0,0,0]
result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
print("This is the encrypted flag!\n{}\n".format("".join(result)))
print(len("3d1905503d1958003d195000015d063d190555113d1900023d195059214d3d19"))

not_encrypted = "a" * 32
encrypted = "00023d1958525c3d1905503d195103113d1905513d1951523d1902033d190556"
encrypted_flag = "0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d"
flag = []
key = []

def fromhex(val: str):
    mul = 1
    sum = 0
    for digit in val[::-1]:
        digit = ord(digit)
        if digit >= ord('a'):
            digit -= ord('a') - 10
        else:
            digit -= ord('0')
        sum += digit*mul
        mul *= 16

    return sum

temp2 = []
temp = []
for i in range(0,64,2):
    temp.append(fromhex(encrypted[i:i+2]))
    temp2.append(fromhex(encrypted_flag[i:i+2]))

print("len of temp = ",len(temp))
encrypted = []
encrypted_flag = []

for i in range(32):
    encrypted.append(temp[i])
    encrypted_flag.append(temp2[i])


for i in range(32):
    key.append(ord(not_encrypted[i]) ^ encrypted[i])

for i in range(32):
    flag.append(chr(key[i]^encrypted_flag[i]))

print(key,sep=' ')
print("".join(flag))
result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
print("This is the encrypted flag!\n{}\n".format("".join(result)))
result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), not_encrypted, key))
print("This is the encrypted flag!\n{}\n".format("".join(result)))
result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), "b&k▬'g;5e8608`f▲∟xgZFxlXE|0⌂e9aj", key))
print("This is the encrypted flag!\n{}\n".format("".join(result)))
print("".join(flag))
