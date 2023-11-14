def check_grammar(sentence):
    valid_punctuation = ['.','!','?']
    return sentence[0].isupper() and sentence[-1] in valid_punctuation