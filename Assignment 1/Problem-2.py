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
        pass
    
    def predict_plain_text(self):
        pass
    


if __name__ == "__main__":

    vigenere = Vigenere(plain_text_path="input.txt", cypher_text_path="output.txt", logging=False)

    print("Hello world")