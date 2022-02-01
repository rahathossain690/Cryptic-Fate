
# @ Rahat Hossain
# @ Problem 1

# Write a program in Python that implements the Vigenere polyalphabetic cipher for English
# text. Your cipher should distinguish lowercase and uppercase letters (i.e. a letter should be
# encrypted differently based on if it is uppercase or lowercase). In your cipher, the
# encryption key, plaintext and the ciphertext should be composed of lowercase and
# uppercase letters. Your program should read the input from a file called input.txt and write
# to a file called output.txt. It should read the encryption key from a file called key.txt. Your
# program should perform the following operations:

# (a) Remove unnecessary characters except A - Z, a - z from the English text in
# input.txt.

# (b) Encode the message using the keyphrase in key.txt.
# (c) Convert the ciphertext produced in step(b) into a message consists of words with 5
# characters and write it into output.txt.
# (d) Decode the ciphertext in output.txt into the original message.



import re

class Vigenere:
    """
    Object declaration for vigenere cypher process
    Encapsulates necessary methods, atributes required for whole opreations
    """

    def __init__(self, plain_text_path="input.txt", key_path="key.txt", cypher_text_path="output.txt", logging=False):
        """
        Contructor function
        creates an object instance
        fixes plain text path, key path, cypher text path and logging option for future usage
        """
        self.plain_text_path = plain_text_path
        self.key_path = key_path
        self.cypher_text_path = cypher_text_path
        self.SIZE = 26 + 26
        self.logging = logging
    
    def encrypt(self):
        """
        Reads plain text, key from file
        removes unnecessary characters
        encrypts by the Vigenere Cypher
        Applies spaces as required
        writes the result in file 
        """
        if self.logging:
            print("Encrypting plain text")
        plain_text = self.remove_unnecessary_chars(self.read_file(self.plain_text_path))
        key = self.remove_unnecessary_chars(self.read_file(self.key_path))
        input_array = [self.char_to_int(i) for i in plain_text]
        key_array = [self.char_to_int(i) for i in key]
        output_array = []
        for i in range(len(input_array)):
            dec_char = None
            if input_array[i] <= 25:
                dec_char = ( input_array[i] + key_array[i % len(key_array)] ) % 25
            else: 
                dec_char = ((input_array[i] + key_array[i % len(key_array)]) % 25) + 25
            output_array.append( dec_char )
        self.write_file(self.cypher_text_path, ' '.join(re.findall('.{1,5}', ''.join([self.int_to_char(i) for i in output_array]))))
        return None
    
    def remove_unnecessary_chars(self, text):
        """
        Uses Regex for removing all the chars except A-Z or a-z
        """
        if self.logging:
            print("Removing unnecessary characters")
        return ''.join(re.findall('[A-Za-z]', text))

    def decrypt(self):
        """
        Reads cypher text, key from file
        Removes spaces 
        decyphers the cypher
        returns the plain text
        """
        if self.logging:
            print("Decrypting cypher text")
        cypher_text = self.read_file(self.cypher_text_path)
        key = self.read_file(self.key_path)
        cypher_text = ''.join(cypher_text.split(' '))
        cypher_text = self.remove_unnecessary_chars(cypher_text)
        input_array = [self.char_to_int(i) for i in cypher_text]
        key_array = [self.char_to_int(i) for i in key]
        output_array = []
        for i in range(len(input_array)):
            dec_char = None
            if input_array[i] <= 25:
                dec_char = ( input_array[i] - key_array[i % len(key_array)] ) % 25
            else: 
                dec_char = ((input_array[i] - key_array[i % len(key_array)] + 25) % 25) + 25
            output_array.append( dec_char )
        return ''.join([self.int_to_char(i) for i in output_array])
    
    def char_to_int(self, char_in):
        """
        Converts from char to int
        """
        if 'A' <= char_in and char_in <= 'Z':
            return ord(char_in) - ord('A') + 26
        else:
            return ord(char_in) - ord('a')
    
    def int_to_char(self, int_in):
        """
        Converts from int to char
        """
        if int_in < 26:
            return chr(int_in + ord('a'))
        else:
            return chr(int_in + ord('A') - 26)
    
    def read_file(self, file_path):
        """
        Reads from file
        returns string
        """
        if self.logging:
            print("Reading from {}".format(file_path))
        result = ""
        with open(file_path,'r') as file:
            result = file.read()
        return result

    
    def write_file(self, file_path, text):
        """
        Writes to file
        """
        if self.logging:
            print("Writing to {}".format(file_path))
        with open(file_path,'w') as file:
            file.write(text)
    
    def compare_with_plain_text(self, text):
        """
        Compares the decyphered text with the input file
        Ignores spaces, characters except A-Z, a-z
        Returns bool
        """
        plain_text = self.read_file(self.plain_text_path)
        i, j = 0, 0
        for i in range(len(plain_text)):
            if(len(text) >= text):
                return False
            if not ('a' <= plain_text[i] and plain_text[i] <= 'z') and not ('A' <= plain_text[i] and plain_text[i] <= 'Z'):
                continue 
            if plain_text[i] != text[j]:
                return False 
            j += 1
        return True


if __name__ == '__main__':
    
    vigenere = Vigenere(plain_text_path="input.txt", key_path="key.txt", cypher_text_path="output.txt", logging=True)
    
    # Encrypting plain text
    vigenere.encrypt()
    print("")

    # Decrypting cypher text
    decyphered = vigenere.decrypt()
    print("")

    # Comparing decyphered text with plain text
    print(vigenere.compare_with_plain_text(decyphered))