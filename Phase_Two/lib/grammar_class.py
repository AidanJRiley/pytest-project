class GrammarStats:
    def __init__(self):
        self.checked = 0
        self.passed = 0

    def check_grammar(self,sentence):
        self.checked += 1
        valid_punctuation = ['.','!','?']
        result =  sentence[0].isupper() and sentence[-1] in valid_punctuation
        if result == True:
            self.passed += 1
        return result
    
    def percentage_good(self):
        result = round(self.passed/self.checked*100)
        return result