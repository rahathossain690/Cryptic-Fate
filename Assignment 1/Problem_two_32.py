# Now take a ciphertext file output.txt generated from Problem 1 and try to generate the
# original message without using the encryption key in key.txt. Your program should
# perform the following operations:
# (a) Print the predicted length of the key. The output may contain more than
# one value.
# (b) The original message or the predicted message based on our algorithm.
# (c) Execute the program on each of the ciphertext generated from Problem 1 and compare

# how close your result to the original message and the key.
# (d) Mark on explanation.

# Hint: Encrypt an arbitrary large message in Problem 1 to generate a ciphertext that is
# sufficiently large enough to help you to predict the original message.


import re
from Problem_one import Vigenere as Vigenere_one

class Vigenere:
    
    def __init__(self, plain_text_path="input.txt", cypher_text_path="output.txt", logging=False):
        """
        Contructor function
        creates an object instance
        fixes plain text path, key path, cypher text path and logging option for future usage
        """
        self.plain_text_path = plain_text_path
        self.cypher_text_path = cypher_text_path
        self.SIZE = 26 + 26
        self.logging = logging
    

    def predict_key_length(self):
        """
        Predicts key length
        """
        if self.logging:
            print("Predicting key length")
        cypher_text = self.remove_unnecessary_chars(self.read_file(self.cypher_text_path))
        possible = list(self.kasiski(cypher_text))
        possible.sort(key=lambda x: -x[1])
        return [item[0] for item in possible if item[0] <= 11]

    def kasiski(self, text):
        """
        Implements key length using kassiski's method
        """
        if self.logging:
            print("Using Kasiski's method")
        diff = []
        diff = diff + self.get_repeat(text, 3)
        diff = diff + self.get_repeat(text, 4)
        diff = diff + self.get_repeat(text, 5)
        diff = list(set(diff))
        if self.logging:
            print("Factorizing repeatation gaps")
        frequency = {}
        for item in diff:
            factors = self.factorize(item)
            for factor in factors:
                if factor not in frequency:
                    frequency[factor] = 1
                else:
                    frequency[factor] += 1
        return frequency.items()

    def get_repeat(self, text, length):
        """
        Calculates distance of repeating substrings
        """
        if self.logging:
            print("Generating repeatation gap for {}".format(length))
        position_dict = {}
        diffs = []
        for i in range(len(text) - length):
            substr = text[i: i + length]
            if substr in position_dict:
                diffs.append(i - position_dict[substr])
            position_dict[substr] = i
        return list(set(diffs))

    def factorize(self, num):
        """
        For factorizing a number
        """
        factors = []
        for i in range(2, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    def predict_plain_text(self, keys):
        """
        Predicts plain text and calculates accuracy
        """
        if self.logging:
            print("Predicting plain text")
        result = []
        for key in keys:
            temp = {}
            temp["length"] = key
            temp["key"] = self.predict_plain_text_of_length(key) 
            temp["accuracy"] = self.accuracy(temp["key"])
            result.append(temp)
        result.sort(key=lambda x: (100 - x["accuracy"] + 0.0001) * x["length"])
        if self.logging:
            print("Result")
            for item in result:
                print("\nKey Length: {} \nKey: {}\nAccuracy: {}%".format(item["length"], item["key"], item["accuracy"]))
        return result

    def accuracy(self, key):
        """
        calculates accuracy
        """
        vig_1 = Vigenere_one(plain_text_path="input.txt", cypher_text_path="output.txt", logging=False)
        fake_cypher = vig_1.encrypt(key=key, write=False)
        real_cypher = self.remove_unnecessary_chars(self.read_file(self.cypher_text_path))
        match = 0
        for i in range(len(fake_cypher)):
            if fake_cypher[i] == real_cypher[i]:
                match += 1
        return ((match * 1.0) / len(fake_cypher)) * 100
    
    def predict_plain_text_of_length(self, length):
        """
        predicts plain text of a certain length
        """
        if self.logging:
            print("Predicting plain text of length {}".format(length))
        cypher_text = self.remove_unnecessary_chars(self.read_file(self.cypher_text_path))
        probable_key = ""
        for i in range(length):
            subscn = [cypher_text[x] for x in range(len(cypher_text)) if i % length == x % length]
            probable_key += self.brutus(subscn)
        return probable_key

    def brutus(self, text):
        """
        Tries to kill ceaser
        """
        if self.logging:
            print("Decyphering the ceaser cypher for subsequence of text")
        frequency = {}
        for c in text:
            if c not in frequency:
                frequency[c] = 1
            else:
                frequency[c] += 1
        every = list(frequency.items())
        every.sort(key=lambda x: -x[1])
        key = every[0][0]
        return self.int_to_char( (self.char_to_int(key) - self.char_to_int('e') + self.SIZE) % self.SIZE  )

    def remove_unnecessary_chars(self, text):
        """
        Uses Regex for removing all the chars except A-Z or a-z
        """
        if self.logging:
            print("Removing unnecessary characters")
        return ''.join(re.findall('[A-Za-z]', text))

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
        with open(file_path,'r', encoding="utf8") as file:
            result = file.read()
        return result
    


if __name__ == "__main__":

    vigenere = Vigenere(plain_text_path="input.txt", cypher_text_path="output.txt", logging=True)

    keys = vigenere.predict_key_length()
    print("")

    vigenere.predict_plain_text(keys)
    print("")