import random
import re
from py.ngram_score import ngram_score
from py.validation import is_sentence

def substitution_cipher(text, key):
    result = ''
    for c in text:
        if 'A' <= c <= 'Z':
            result += key[ord(c) - 65].upper()
        elif 'a' <= c <= 'z':
            result += key[ord(c) - 97]
        else:
            result += c
    return result


def decrypt_substitution_cipher(text, key):

    result = ''
    new_key = [''] * 26
    for i, c in enumerate(key):
        new_key[ord(c) - 97] = chr(i + 97)

    for c in text:
        if 'A' <= c <= 'Z':
            result += new_key[ord(c) - 65].upper()
        elif 'a' <= c <= 'z':
            result += new_key[ord(c) - 97]
        else:
            result += c

    return result


def brute_force_substitution_cipher(text):

    fitness = ngram_score('py/quadgrams.txt')
    maxKey = list('abcdefghijklmnopqrstuvwxyz')
    maxScore = -99e9
    parentScore, parentKey = maxScore, maxKey[:]
    i = 0
    while 1:
        i = i + 1
        random.shuffle(parentKey)
        deciphered = decrypt_substitution_cipher(text, parentKey)
        clean_text = "".join(filter(str.isalpha, deciphered)).upper()
        parentScore = fitness.score(clean_text)
        count = 0
        while count < 1000:
            a = random.randint(0, 25)
            b = random.randint(0, 25)
            child = parentKey[:]
            # swap two characters in the child
            child[a], child[b] = child[b], child[a]
            deciphered = decrypt_substitution_cipher(text, child)
            clean_text = "".join(filter(str.isalpha, deciphered)).upper()
            score = fitness.score(clean_text)
            # if the child was better, replace the parent with it
            if score > parentScore:
                parentScore = score
                parentKey = child[:]
                print(parentScore)
                count = 0
            count = count + 1
        # keep track of best score seen so far
        if parentScore > maxScore:
            maxScore, maxKey = parentScore, parentKey[:]
            deciphered = decrypt_substitution_cipher(text, maxKey)
            res, flag = is_sentence(deciphered)
            if flag:
                print(res)
                print(maxKey)
                return res






#
# # Original text and key for demonstration
#
# text = """
# For a recap of how substitution ciphers work, see here.
#
# The Simple substitution cipher is one of the simplest ciphers, simple enough that it can usually be broken with pen and paper in a few minutes. On this page we will focus on automatic cryptanalysis of substitution ciphers, i.e. writing programs to solve these ciphers for us.
#
# The substitution cipher is more complicated than the Caesar and Affine ciphers. In those cases, the number of keys were 25 and 311 respectively. This allowed a brute force solution of trying all possible keys. The number of keys possible with the substitution cipher is much higher, around 2^88 possible keys. This means we cannot test them all, we have to 'search' for good keys.
#
# We will be using a 'hill-climbing' algorithm to find the correct key. For this approach, we need a way of determining how similar a piece of text is to english text. This is called rating the 'fitness' of the text. A piece of text very similar to english will get a high score (a high fitness), while a jumble of random characters will get a low score (a low fitness). For this we will use a fitness measure based on quadgram statistics. For a guide on how to generate quadgram statistics, and some python code for rating the fitness of text, see this tutorial. This method works by first determining the statistics of english text, then calculating the probability that the ciphertext comes from the same distribution. An incorrectly deciphered (i.e. using the wrong key) message will probably contain sequences e.g. 'QKPC' which are very rare in normal english. In this way we can rank different decryption keys, the decryption key we want is the one that produces deciphered text with the highest likelyhood.
#
# The hill-climbing algorithm looks like this:
#
# Generate a random key, called the 'parent', decipher the ciphertext using this key. Rate the fitness of the deciphered text, store the result.
# Change the key slightly (swap two characters in the key at random), measure the fitness of the deciphered text using the new key.
# If the fitness is higher with the modified key, discard our old parent and store the modified key as the new parent.
# Go back to 2, unless no improvement in fitness occurred in the last 1000 iterations.
# As this cycle proceeds, the deciphered text gets fitter and fitter, the key becomes better until either the solution appears, or, the solution is not found. In this case the run has failed and must be repeated with a different starting key. This means the hill-climbing algorithm is stuck in a 'local maximum', where there are no simple changes that can be made to the key to improve fitness, and yet it is not at the true solution. If this happens you can run the algorithm again with a different parent in the hope it may reach the true solution this time. In the implementation below, we may restart the algorithm 100's of times in the search for the best key.
# """
# key = "xnyahpogzqwbtsflrcvmuekjdi"
# # Decrypt the key with itself as a demonstration
#
#
# encrypted = substitution_cipher(text, key)
# print(encrypted)
# print("-----------------------------------------------------------------------------------")
# brute_force_substitution_cipher(encrypted)
#
#
