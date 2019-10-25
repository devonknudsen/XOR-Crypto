# Persians: Sydney Anderson, Tram Doan, Devon Knudsen, Zackary Phillips, Promyse Ward, James Wilson
# GitHub Repo URL: https://github.com/devonknudsen/XOR-Crypto/edit/master/xor.py
# Written in Python 3.5.2

# take a message (either plaintext or ciphertext)
# takes a key (same size as message)
# each bit of message is xor with each bit of key, one at a time

from sys import stdin, stdout

# takes in key and msg, xors them, 
# and prints out characters to stdout
def Xor(msg, key):

    if DEBUG:
        print("key length: {}".format(len(key)))
        print("msg length: {}".format(len(msg)))
        print("---")
        print("KEY: {}".format(key))
        print("MSG: {}".format(msg))
        print("---")

    # xor each byte of msg with key
    for i in range(0,len(msg)):

        # xor the bytes to recieve the integer value
        # i%len(key) should handle if len(key) < len(msg)
        intV = (msg[i] ^ key[i%len(key)])

        # encode the character to bytes
        byte = bytes(chr(intV), "iso-8859-1")

        # write the byte to stdout
        stdout.buffer.write(byte)

        if DEBUG:
            print("-"*23)
            print("msg int: \t{}".format(msg[i%len(key)]))
            print("key int: \t{}".format(key[i]))
            print("---")
            print("xor int: \t{}".format(intV))
            print("xor byte char:\t{}".format(byte))

### MAIN CODE ###
DEBUG = False

# open key file and read in binary mode
key = open('key2', "rb")

# remove new lines from byte string
key = key.read().rstrip(bytes("\n", "ascii"))

# read from stdin and remove new lines from byte string
msg = stdin.buffer.read().rstrip(bytes("\n", "ascii"))

# xor key and msg
Xor(msg,key)
