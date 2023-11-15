class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words_read = 0

    def format(self):
        return f"{self.title.title()}: {self.contents}"
    
    def count_words(self):
        return len(self.format().split())
    
    def reading_time(self,wpm):
        if self.count_words() < wpm:
            return 1
        return round(self.count_words() / wpm)

    
    def reading_chunk(self,wpm,minutes):
        words_to_read = wpm * minutes
        entry_as_list = self.format().split()
        if self.words_read + words_to_read > self.count_words():
            start_point = self.words_read
            self.words_read = 0
            return ' '.join(entry_as_list[start_point:])
        result = ' '.join(entry_as_list[self.words_read:self.words_read+words_to_read])
        self.words_read = self.words_read + words_to_read
        return result
        

