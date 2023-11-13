def make_snippet(text):
    text_to_list = text.split()
    if len(text_to_list) > 5:
        new_text = ' '.join(text_to_list[0:5]) + '...'
    else:
        new_text = text
    return new_text

def count_words(sentence):
    return len(sentence.split())