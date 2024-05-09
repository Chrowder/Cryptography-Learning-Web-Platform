import math
from collections import Counter

def calculate_entropy(text):

    # Count each character
    char_count = Counter(text)
    total_chars = len(text)

    # Calculate probabilities
    probabilities = [count / total_chars for count in char_count.values()]

    # Calculate Shannon entropy
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)

    return entropy




def text_to_binary(text):
    # Filter to include only alphabetic characters and convert each to binary
    return ''.join(format(ord(char), '08b') for char in text if char.isalpha())




def calculate_ber(original_text, corrupted_text):
    original_binary = text_to_binary(original_text)
    corrupted_binary = text_to_binary(corrupted_text)


    min_length = min(len(original_binary), len(corrupted_binary))
    original_binary = original_binary[:min_length]
    corrupted_binary = corrupted_binary[:min_length]


    bit_errors = sum(o != c for o, c in zip(original_binary, corrupted_binary))


    total_bits = min_length
    ber = bit_errors / total_bits if total_bits > 0 else 0

    return ber



# original_text = "Example text for entropy calculation."
# corrupted_text = "Excmple text for entropy calculatton."
#
# ber = calculate_ber(original_text, corrupted_text)
# print(ber)
