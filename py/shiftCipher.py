from py.validation import is_sentence

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


# def brute_force_caesar_cipher(text):
#     array = [0] * 26
#     for shift in range(1, 27):
#         decrypted = shift_cipher(text, -shift)
#         array[shift - 1] = is_sentence(decrypted)
#     max_value = max(array)
#     max_index = array.index(max_value) + 1
#     print(max_index)
#     result = shift_cipher(text, -max_index)
#     return result

def brute_force_shift_cipher(text):
    array = [0] * 26
    for shift in range(1, 27):
        decrypted = shift_cipher(text, -shift)
        decrypted_text, flag = is_sentence(decrypted)
        if flag:
            return decrypted_text