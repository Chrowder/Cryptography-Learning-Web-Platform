from validation import count_words_in_text

def shift_cipher(text, key):
    result = ''
    key = key % 26
    if key < 0:
        key += 26
    for c in text:
        if 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') + key) % 26 + ord('A'))
        elif 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
        else:
            result += c
    return result


def brute_force_caesar_cipher(text):
    array = [0] * 26
    for shift in range(1, 27):
        decrypted = shift_cipher(text, -shift)
        array[shift - 1] = count_words_in_text(decrypted)
    max_value = max(array)
    max_index = array.index(max_value)
    result = shift_cipher(text, -max_index)
    return result