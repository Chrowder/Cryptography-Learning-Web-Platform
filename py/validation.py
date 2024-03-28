# I forgot to import the re module for regular expressions. Let's correct that.
import re

def count_words_in_text(text):
    common_words = ["the", "and", "of", "to", "in", "a", "is", "that", "it", "for"]
    # Using regular expressions to find words
    words = re.findall(r'\b(\w+)\b', text.lower())
    count = sum(1 for word in words if word in common_words)
    return count

# Example usage of the updated count_words_in_text function
text = "This is a simple test of the countWordsInText function, aiming to see how it performs."
count_words_in_text(text)
