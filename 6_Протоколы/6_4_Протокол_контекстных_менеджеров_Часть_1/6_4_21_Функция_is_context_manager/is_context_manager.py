''' Первый вариант решения'''
def is_context_manager(obj):
    try:
        if obj.__enter__ and obj.__exit__:
            return True
    except:
        return False
''' Второй вариант решения'''    
# def is_context_manager(obj):
#     return hasattr(obj, '__enter__') and hasattr(obj, '__exit__')