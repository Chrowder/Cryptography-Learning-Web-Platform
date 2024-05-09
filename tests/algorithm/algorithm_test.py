import pytest
import time
from MyCipher.permutationCipher import permutation_cipher, decrypt_permutation_cipher, brute_force_permutation_cipher, brute_force_permutation_cipher_old
from MyCipher.shiftCipher import shift_cipher, brute_force_shift_cipher
from MyCipher.substitutionCipher import substitution_cipher,decrypt_substitution_cipher, brute_force_substitution_cipher
from MyCipher.Accuracy_Testing import calculate_ber


with open("/Users/chrowder/Documents/PC/code/Python/Pycharm/COMP390_py/tests/algorithm/hamlet.txt", 'r', encoding='utf-8') as file:
    hamlet = file.read()

quadgrams = '/Users/chrowder/Documents/PC/code/Python/Pycharm/COMP390_py/MyCipher/quadgrams.txt'



def test_shift_5():
    hamlet_shift_5 = shift_cipher(hamlet, 5)
    hamlet_cracked, key = brute_force_shift_cipher(hamlet_shift_5)
    assert hamlet_cracked == hamlet

def test_shift_10():
    hamlet_shift_10 = shift_cipher(hamlet, 10)
    hamlet_cracked, key = brute_force_shift_cipher(hamlet_shift_10)
    assert hamlet_cracked == hamlet

def test_shift_15():
    hamlet_shift_15 = shift_cipher(hamlet, 15)
    hamlet_cracked, key = brute_force_shift_cipher(hamlet_shift_15)
    assert hamlet_cracked == hamlet


def test_substitution_apyotjesrmgwnkcfhdlxbzivqu():
    hamlet_substitution_apyotjesrmgwnkcfhdlxbzivqu = substitution_cipher(hamlet, 'apyotjesrmgwnkcfhdlxbzivqu')
    hamlet_cracked, key = brute_force_substitution_cipher(hamlet_substitution_apyotjesrmgwnkcfhdlxbzivqu, quadgrams)
    ber = calculate_ber(hamlet, hamlet_cracked)
    print(ber)
    assert hamlet_cracked == hamlet

def test_substitution_zyxwvutsrqponmlkjihgfedcba():
    hamlet_substitution_zyxwvutsrqponmlkjihgfedcba = substitution_cipher(hamlet, 'zyxwvutsrqponmlkjihgfedcba')
    hamlet_cracked, key = brute_force_substitution_cipher(hamlet_substitution_zyxwvutsrqponmlkjihgfedcba, quadgrams)
    ber = calculate_ber(hamlet, hamlet_cracked)
    print(ber)
    assert hamlet_cracked == hamlet


def test_substitution_audszhwrgfjylcpkbnqomtexvi():
    hamlet_substitution_audszhwrgfjylcpkbnqomtexvi = substitution_cipher(hamlet, 'audszhwrgfjylcpkbnqomtexvi')
    hamlet_cracked, key = brute_force_substitution_cipher(hamlet_substitution_audszhwrgfjylcpkbnqomtexvi, quadgrams)
    ber = calculate_ber(hamlet, hamlet_cracked)
    print(ber)
    assert hamlet_cracked == hamlet


def test_substitution_esovnwbazidljyrcqpmfugxhtk():
    hamlet_substitution_esovnwbazidljyrcqpmfugxhtk = substitution_cipher(hamlet, 'esovnwbazidljyrcqpmfugxhtk')
    hamlet_cracked, key = brute_force_substitution_cipher(hamlet_substitution_esovnwbazidljyrcqpmfugxhtk, quadgrams)
    ber = calculate_ber(hamlet, hamlet_cracked)
    print(ber)
    assert hamlet_cracked == hamlet




def test_permutation_351642():
    hamlet_permutation_351642 = permutation_cipher(hamlet, [3, 5, 1, 6, 4, 2])
    hamlet_cracked, key = brute_force_permutation_cipher(hamlet_permutation_351642, quadgrams)
    assert hamlet_cracked == hamlet


def test_permutation_43521():
    hamlet_permutation_43521 = permutation_cipher(hamlet, [4, 3, 5, 2, 1])
    hamlet_cracked, key = brute_force_permutation_cipher(hamlet_permutation_43521, quadgrams)
    assert hamlet_cracked == hamlet


def test_permutation_7431652():
    hamlet_permutation_7431652 = permutation_cipher(hamlet, [7, 4, 3, 1, 6, 5, 2])
    hamlet_cracked, key = brute_force_permutation_cipher(hamlet_permutation_7431652, quadgrams)
    assert hamlet_cracked == hamlet

def test_permutation_624351():
    hamlet_permutation_624351 = permutation_cipher(hamlet, [6, 2, 4, 3, 5, 1])
    hamlet_cracked, key = brute_force_permutation_cipher(hamlet_permutation_624351, quadgrams)
    assert hamlet_cracked == hamlet

def test_permutation_35168427():
    hamlet_permutation_35168427 = permutation_cipher(hamlet, [3, 5, 1, 6, 8, 4, 2, 7])
    hamlet_cracked, key = brute_force_permutation_cipher(hamlet_permutation_35168427, quadgrams)
    assert hamlet_cracked == hamlet



def test_permutation_43521_old():
    hamlet_permutation_43521 = permutation_cipher(hamlet, [4, 3, 5, 2, 1])
    hamlet_cracked, key = brute_force_permutation_cipher_old(hamlet_permutation_43521)
    assert hamlet_cracked == hamlet

def test_permutation_351642_old():
    hamlet_permutation_351642 = permutation_cipher(hamlet, [3, 5, 1, 6, 4, 2])
    hamlet_cracked, key= brute_force_permutation_cipher_old(hamlet_permutation_351642)
    assert hamlet_cracked == hamlet


def test_permutation_7431652_old():
    hamlet_permutation_7431652 = permutation_cipher(hamlet, [7, 4, 3, 1, 6, 5, 2])
    hamlet_cracked, key = brute_force_permutation_cipher_old(hamlet_permutation_7431652)
    assert hamlet_cracked == hamlet

def test_permutation_624351_old():
    hamlet_permutation_624351 = permutation_cipher(hamlet, [6, 2, 4, 3, 5, 1])
    hamlet_cracked, key = brute_force_permutation_cipher_old(hamlet_permutation_624351)
    assert hamlet_cracked == hamlet

