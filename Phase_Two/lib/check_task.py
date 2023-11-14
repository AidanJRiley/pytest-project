def check_task(text):
    if text == "" or type(text) != str:
        raise Exception("Please insert valid text")
    phrase = '#TODO'
    return phrase in text