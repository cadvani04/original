# author: Curran Advani
# date: March 16th, 2023
# file: steganography.py creates the class Codec and Caesar Cypher
# input: code for the encode text and decode data
# output: displays the encoded binary and decoded text messages in a string
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher


class Steganography():

    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        print(image)  # for debugging
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)
        # convert into binary
        if codec == 'binary':
            self.codec = Codec()
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            self.codec = HuffmanCodes()
        binary = self.codec.encode(message + self.delimiter)
        print(binary)
        # check if possible to encode the message
        num_bytes = ceil(len(binary) // 8) + 1
        if num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            def binaryToDecimal(num):
                decimal, i = 0, 0
                while (num != 0):
                    dec = num % 10
                    decimal = decimal + dec * pow(2, i)
                    num = num // 10
                    i += 1
                return decimal
            print("Bytes to encode:", num_bytes)
            self.text = message
            self.binary = binary
            # your code goes here
            bit_index = 0
            for rows in image:
                for columns in rows:
                    for nums in columns:
                        if bit_index >= 8:
                            break
                        if nums % 2 == 0 and binary[bit_index] == "1": #check if the last part of binary of image is a 1 or 0 and change or keep same accordingly
                            nums += 1
                        elif nums % 2 != 0 and binary[bit_index] == "0": #check if the last part of binary of image is a 1 or 0 and change or keep same accordingly
                            nums -= 1
                        bit_index += 1

            #your code goes here
            # you may create an additional method that modifies the image array
            cv2.imwrite(fileout, image)

    def decode(self, filein, codec):
        image = cv2.imread(filein)
        image = np.array(image)
        # print(image) # for debugging
        flag = True

        # convert into text
        if codec == 'binary':
            self.codec = Codec()
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            if self.codec is None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False

            binary_data = ''
            for x in range(len(image)):
                for y in range(len(image[x])):
                    for z in range(len(image[x][y])):
                        if image[x][y][z] % 2 == 0:
                            binary_data += "0"
                        else:
                            binary_data += "1"
            self.text = self.codec.decode(binary_data)
            self.binary = self.codec.encode(self.text + self.delimiter)






        # your code goes here
        # you may create an additional method that extract bits from the image array

        '''binary_data = self.codec.encode()
        # update the data attributes:
        self.text = self.codec.decode(binary_data)
        self.binary = self.codec.encode()'''

    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()
if __name__ == '__main__':
    s = Steganography()

    s.encode('fractal.jpg', 'fractal.png', 'hello', 'binary')
    #s.encode('redbox (1).jpg', 'redbox.png', 'hello', 'binary')
    # NOTE: binary should have a delimiter and text should not have a delimiter
    print(s.text)
    print(s.binary)
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'

    s.decode('fractal.png', 'binary')
    s.decode('redbox.png', 'binary')
    #print(s.text)
    #print(s.binary)
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'
    print('Everything works!!!')

    s.encode('fractal.jpg', 'fractal.png', 'hello', 'caesar')
    #s.encode('redbox (1).jpg', 'redbox.png', 'hello', 'binary')
    # NOTE: binary should have a delimiter and text should not have a delimiter
    print(s.text)
    print(s.binary)
    assert s.text == 'hello'
    assert s.binary == '011010110110100001101111011011110111001000100110'

    s.decode('fractal.png', 'caesar')
    #s.decode('redbox.png', 'binary')
    print(s.text)
    print(s.binary)
    assert s.text == 'hello'
    assert s.binary == '011010110110100001101111011011110111001000100110'
    print('Everything works!!!')