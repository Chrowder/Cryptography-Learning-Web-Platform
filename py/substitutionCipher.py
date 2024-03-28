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


# Original text and key for demonstration
text = "abcdefghijklmnopqrstuvwxyz"
key = "xnyahpogzqwbtsflrcvmuekjdi"
# Decrypt the key with itself as a demonstration
result = decrypt_substitution_cipher(key, key)
print(result)
