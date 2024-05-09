from itertools import permutations
import re
from MyCipher.validation import is_sentence
from MyCipher.ngram_score import ngram_score

def permutation_cipher(text, key):
    length_text = len(text)
    length_key = len(key)
    if length_text % length_key != 0:
        padding_length = length_key - (length_text % length_key)
        text += '*' * padding_length

    groups = [text[i:i + length_key] for i in range(0, length_text, length_key)]

    enc = ""
    for group in groups:
        encrypted_group = [''] * length_key
        for i, index in enumerate(key):
            encrypted_group[i] = group[index - 1]
        enc += ''.join(encrypted_group)

    return enc



def decrypt_permutation_cipher(text, key):
    new_key = [None] * len(key)

    for i, index in enumerate(key):
        new_key[index - 1] = i + 1
        
    dec = permutation_cipher(text, new_key)
    dec = re.sub(r'\*+$', '', dec)
    return dec



def generate_permutations(n):
    if n < 1:
        return []
    else:
        numbers = list(range(1, n + 1))
        all_permutations = list(permutations(numbers))
        all_permutations = all_permutations[0:]
        return all_permutations


def brute_force_permutation_cipher_old(text):
    flag = False
    n = 2
    while flag == False:
        possible_key = generate_permutations(n)
        for key in possible_key:
            # print(key)
            dec = decrypt_permutation_cipher(text, key)
            res, flag = is_sentence(dec)
            if flag:
                res = re.sub(r'\*+$', '', res)
                return res, key
        n += 1


def brute_force_permutation_cipher(text, quadgrams='MyCipher/quadgrams.txt'):
    flag = False
    n = 2
    count = 0
    fitness = ngram_score(quadgrams)
    maxScore = -99e9
    mostLikely_key = [1]
    mostLikely_dec = ""
    while flag == False:
        possible_key = generate_permutations(n)
        for key in possible_key:
            count += 1
            # print(key)
            dec = decrypt_permutation_cipher(text, key)
            clean_text = "".join(filter(str.isalpha, dec)).upper()
            clean_text = clean_text[:1000]
            score = fitness.score(clean_text)
            if score > maxScore:
                maxScore = score
                mostLikely_key = key
                mostLikely_dec = dec
                count = 0
            if count > 500:
                count = 0
                res, flag = is_sentence(mostLikely_dec)
                if flag:
                    res = re.sub(r'\*+$', '', res)
                    mostLikely_key = [str(num) for num in mostLikely_key]
                    mostLikely_key = ' '.join(mostLikely_key)
                    return res, mostLikely_key
        n += 1


#
# text = """
# The Python replication of the countWordsInText function successfully identifies and counts common English words within a given text.
# For the example text, "This is a simple tests of the countWordsInText function, aiming to see how it performs,"
# it found that 6 of the words are among the specified common words.
# This function can now be used in conjunction with the earlier brute-force Caesar cipher decryption to more accurately identify the correct decryption by maximizing the number of recognizable words.
# """
#
# key = [3, 5, 1, 6, 4, 2]
# enText = permutation_cipher(text, key)
# print(enText)
# deText = decrypt_permutation_cipher(enText, key)
# print(deText)
# brText, new_key = brute_force_permutation_cipher(enText)
# print(brText)
# print(new_key)