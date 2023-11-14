def grammar_check(text):
    valid_punctuation = ['.','?','!']
    capitalised = text[0].isupper()
    end_punctuation = text[-1] in valid_punctuation

    return capitalised and end_punctuation