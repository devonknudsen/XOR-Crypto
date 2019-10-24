# take a message (either plaintext or ciphertext)
# takes a key (same size as message)
# each bit of message is xor with each bit of key, one at a time

import sys

def Xor(msg, key):
    cipher = ""
    if DEBUG:
        print("key length: {}".format(len(key)))
        print("msg length: {}".format(len(msg)))
        print("---")
        print("KEY: {}".format(key))
        print("MSG: {}".format(msg))
        print("---")

    # x allows repeat of key
    x = 0
    for i in range(0,len(msg)):

        #print(x)
        if x == len(key):
            x = 0

        msgint = ord(msg[i])
        keyint = ord(key[x])
        

        if DEBUG:
            print("msg char: \t{}".format(msg[i]))
            print("key char: \t{}".format(key[x]))
            print("---")
            print("msg int: \t{}".format(msgint))
            print("key int: \t{}".format(keyint))
            print("----")

        msgbin = bin(msgint)
        keybin = bin(keyint)

        if DEBUG:
            print("msg bin: \t{}".format(msgbin))
            print("key bin: \t{}".format(keybin))
            print("---")

        num = int(msgbin,2) ^ int(keybin,2)
        binary = (bin(num)[2:].zfill(len(msgbin)))
        chary = chr(num)

        if DEBUG:
            print("text bin: \t{}".format(binary))
            print("text int: \t{}".format(num))
            print("text char: \t{}".format(chary))
            print("-"*46)

        x += 1
        cipher += chary
    return cipher

# main
DEBUG = False
msg = sys.stdin.read().rstrip('\n')
key = [line.rstrip('\n') for line in open('key2')]
key = ''.join(key)

print(Xor(msg,key))
