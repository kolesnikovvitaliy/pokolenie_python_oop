''' Первый вариант решения'''
class Pagination:
    def __init__(self, text: list[str], num: int):
        self.num = num
        self.pages = text

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, text):
        k = 1
        self._pages = dict()
        while text:
            self._pages.setdefault(k, []).extend(text[:self.num])
            k += 1
            text = text[self.num:]
        self.total_pages = max(self.pages.keys())
        self.current_page = 1

    def get_visible_items(self):
        '''Отображение текущей страницы'''
        return self.pages[self.current_page]

    def prev_page(self):
        '''вернуться к предыдущей странице'''
        num = self.current_page - 1
        self.go_to_page(num)
        return self

    def next_page(self):
        '''перейти к следующей странице'''
        num = self.current_page + 1
        self.go_to_page(num)
        return self

    def first_page(self):
        '''вернуться к первой странице'''
        self.current_page = 1

    def last_page(self):
        '''перейти к последней странице'''
        self.current_page = self.total_pages

    def go_to_page(self, num: int):
        '''перейти к странице с указанным номером (
            1 — первая страница,
            2 — вторая страница, и так далее)'''
        if num > self.total_pages:
            return self.last_page()
        elif num < 1:
            return self.first_page()
        else:
            self.current_page = num
''' Второй вариант решения'''    
# class Pagination:
#     def __init__(self, data, size):
#         self.pages = [data[i: i+size] for i in range(0, len(data), size)]
#         self.total_pages = len(self.pages)
#         self.current_page = 1

#     def prev_page(self):
#         self.current_page = max(1, self.current_page - 1)
#         return self

#     def next_page(self):
#         self.current_page = min(self.total_pages, self.current_page + 1)
#         return self

#     def first_page(self):
#         self.current_page = 1

#     def last_page(self):
#         self.current_page = self.total_pages

#     def go_to_page(self, page):
#         self.current_page = max(1, min(page, self.total_pages))

#     def get_visible_items(self):
#         return self.pages[self.current_page - 1]