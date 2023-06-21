''' Первый вариант решения'''
class Wordplay:
    def __init__(self, word=[]):
        self.word = word
        self.words = [i for i in self.word if len(self.word)]
   
    def add_word(self, text):
        if text not in self.words:
            self.words.append(text)

    def words_with_length(self, n):
         return list(filter(lambda x: len(x) == n, self.words))
    def only(self, *args):
         return list(filter(lambda x:  x not in [x for i in x if i not in args], self.words))
    def avoid(self, *args):
         return list(filter(lambda x: x not in [x for i in args if i in x], self.words))

''' Второй вариант решения'''    
# class Wordplay:
#     def __init__(self, words=()):
#         self.words = []
#         self.words.extend(words)
        
#     def add_word(self, word):
#         self.words.append(word)
        
#     def words_with_length(self, n):
#         return [w for w in self.words if len(w) == n]
    
#     def only(self, *args):
#         return [w for w in self.words if set(w) <= set(args)]

#     def avoid(self, *args):
#         return [w for w in self.words if len(set(w) & set(args)) == 0]