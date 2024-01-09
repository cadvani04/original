# author: Curran Advani
# date: March 16th, 2023
# file: codec.py creates the class Codec and Caesar Cypher
# input: code for the encode text and decode data
# output: displays the encoded binary and decoded text messages in a string

# codecs
import numpy as np


class Codec():

    def __init__(self):
        self.name = 'binary'
        self.delimiter = ''

    # convert text or numbers into binary form
    def encode(self, text): # look at 8 bytes at a time
        if type(text) == str:
            return ''.join([format(ord(i), "08b") for i in text])
        else:
            print('Format error')

    # convert binary data into text
    def decode(self, data):
        binary = []
        for x in range(0, len(data), 8):
            byte = data[x: x + 8]
            if byte == self.encode(self.delimiter):
                break
            binary.append(byte)
        text = ''
        for byte in binary:
            text += chr(int(byte, 2))
        return text


class CaesarCypher(Codec):

    def __init__(self, shift=3):
        self.name = 'caesar'
        self.delimiter = ''
        self.shift = shift
        self.chars = 256  # total number of characters

    # convert text into binary form
    # your code should be similar to the corresponding code used for Codec
    def encode(self, text):
        data = ''
        for x in text:
            data += chr((ord(x) + self.shift) % 256)
        if type(text) == str:
            return ''.join([format(ord(i), "08b") for i in data])
        else:
            print('Format error')
        return data

        # your code goes here

    # convert binary data into text
    # your code should be similar to the corresponding code used for Codec
    def decode(self, data):
        text = ''
        text1 = ''
        # for char in data:
        # text += chr((ord(char) - self.shift) % 256)
        binary = []
        for i in range(0, len(data), 8):  # look at 8 bytes at a time
            byte = data[i: i + 8]
            if byte == self.encode(self.delimiter):
                break
            binary.append(byte)
        for byte in binary:
            text += chr(int(byte, 2))
        for x in text:
            text1 += chr((ord(x) - self.shift) % 256)
        return text1


# a helper class used for class HuffmanCodes that implements a Huffman tree
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = freq
        self.symbol = symbol
        self.code = ''

    # convert text into binary form
    def encode(self, text):
        data = ''
        # your code goes here
        # you need to make a tree
        # and traverse it
        return data

    # convert binary data into text
    def decode(self, data):
        text = ''
        # your code goes here
        # you need to traverse the tree
        return text


# driver program for codec classes
if __name__ == '__main__':
    text = 'hello'
    # text = 'Casino Royale 10:30 Order martini'
    print('Original:', text)

    c = Codec()
    binary = c.encode(text + c.delimiter)
    # NOTE: binary should have a delimiter and text should not have a delimiter
    print('Binary:', binary)  # should print '011010000110010101101100011011000110111100100011'
    data = c.decode(binary)
    print('Text:', data)  # should print 'hello'

    cc = CaesarCypher()
    binary = cc.encode(text + cc.delimiter)
    # NOTE: binary should have a delimiter and text should not have a delimiter
    print('Binary:', binary)
    data = cc.decode(binary)
    print('Text:', data)  # should print 'hello'

    # h = HuffmanCodes()
    # binary = h.encode(text + h.delimiter)
    # # NOTE: binary should have a delimiter and text should not have a delimiter
    # print('Binary:', binary)
    # data = h.decode(binary)
    # print('Text:', data)     # should print 'hello'