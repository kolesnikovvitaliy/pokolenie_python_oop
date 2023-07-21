''' Первый вариант решения'''
def log_for(logfile, date_str):
    with (
        open(logfile, mode='r', encoding='utf-8') as read_file,
        open(f'log_for_{date_str}.txt', mode='w', encoding='utf-8') as write_file,
        ):
        text = '\n'.join(map(lambda y: y[11:],filter(lambda x: date_str in x, map(str,read_file.read().split('\n')))))
        write_file.write(text)
''' Второй вариант решения'''    
# def log_for(logfile, date_str): 
#     with open(f'log_for_{date_str}.txt', 'w') as result:
#         for line in open(logfile):
#             if date_str in line:
#                 date, info = line.split(' ', 1)
#                 result.write(info)