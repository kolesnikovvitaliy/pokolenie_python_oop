''' Первый вариант решения'''
import sys
class UpperPrint:
    def __enter__(self):
        self.output = sys.stdout
        sys.stdout = open('output.txt', 'w')        
    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.close()
        sys.stdout = self.output
        with open('output.txt', mode='r') as text:
            print(text.read().strip().upper())
''' Второй вариант решения'''    
# import sys

# class UpperPrint:
#     def __enter__(self):
#         self.w = sys.stdout.write
#         sys.stdout.write = lambda t: self.w(t.upper())

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         sys.stdout.write = self.w