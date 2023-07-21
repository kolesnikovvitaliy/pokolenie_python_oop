''' Первый вариант решения'''
def non_closed_files(files):
    for i in files:
        if i.closed:
            continue
        yield i
''' Второй вариант решения'''    
# def non_closed_files(files):
#     return [file for file in files if not file.closed]