import nltk
import re

nltk.download('words')

from nltk.corpus import words
word_list = words.words()

def is_word(word):
    return word.lower() in word_list


def is_sentence(text):
    words = re.findall(r'\b\w+\b', text)
    meaningful_count = 0
    words = words[:100]

    for word in words:
        if is_word(word):
            meaningful_count += 1
    if meaningful_count / len(words) > 0.5:
        return text, True
    else:
        return "", False


#
#
# text = "The Python replication of the   successfully identifies and counts common English words within a given text. For the example text"
# count, flag = is_sentence(text)
# print(count)

# Wkh Sbwkrq uhsolfdwlrq ri wkh frxqwZrugvLqWhaw ixqfwlrq vxffhvvixoob lghqwlilhv dqg frxqwv frpprq Hqjolvk zrugv zlwklq d jlyhq whaw. Iru wkh hadpsoh whaw, "Wklv lv d vlpsoh whvw ri wkh frxqwZrugvLqWhaw ixqfwlrq, dlplqj wr vhh krz lw shuirupv," lw irxqg wkdw 6 ri wkh zrugv duh dprqj wkh vshflilhg frpprq zrugv. Wklv ixqfwlrq fdq qrz eh xvhg lq frqmxqfwlrq zlwk wkh hduolhu euxwh-irufh Fdhvdu flskhu ghfubswlrq wr pruh dffxudwhob lghqwlib wkh fruuhfw ghfubswlrq eb pdalplclqj wkh qxpehu ri uhfrjqlcdeoh zrugv