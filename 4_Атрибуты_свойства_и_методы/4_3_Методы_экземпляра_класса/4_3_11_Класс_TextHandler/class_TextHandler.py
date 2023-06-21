''' Первый вариант решения'''
class TextHandler:
    def __init__(self):
        self.words = list()

    def add_words(self, text):
        [self.words.append(i) for i in text.split()]

    def get_shortest_words(self):
        if len(self.words) > 0:
            min_len_text = min(map(len, self.words))
            return list(filter(lambda x: len(x) <= min_len_text, self.words))
        return self.words

    def get_longest_words(self):
        if len(self.words) > 0:
            max_len_text = max(map(len, self.words))
            return list(filter(lambda x: len(x) == max_len_text, self.words))
        return self.words



''' Второй вариант решения'''    
# class TextHandler:
#     def __init__(self):
#         self.words = []
        
#     def add_words(self, text):
#         self.words += text.split()
        
#     def get_shortest_words(self):
#         return [w for w in self.words if len(w) == min(map(len, self.words))]
      
#     def get_longest_words(self):
#         return [w for w in self.words if len(w) == max(map(len, self.words))]

