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

# Example usage
# key = [3,5,1,6,4,2]
# key = "351642"
# key = [int(digit) for digit in key]
# text = "shesellsseashellsbytheseashore"
#
# print(permutation_cipher(text, key))
