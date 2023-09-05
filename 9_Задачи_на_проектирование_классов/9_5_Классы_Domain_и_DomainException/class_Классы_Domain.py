''' Первый вариант решения'''
import re


class DomainException(Exception):
    pass


class Domain:
    def __init__(self, string):
        self.domain = string

    @staticmethod
    def is_valid_domain(string):
        if '@' in string:
            regex_email = re.compile(r"^[a-z]+@([\w]+\.)+[\w]{2,4}$")
            if regex_email.match(string):
                return string.split('@')[1]
        else:
            regex_url = re.compile(
                        r"(\w+://)?"
                        r"(([\w-]+)\.(\w+)[a-z]$)"
                        )
            if regex_url.match(string):
                return string
        raise DomainException('Недопустимый домен, url или email')

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, string):
        self._domain = self.is_valid_domain(string)

    def __str__(self):
        return f'{self.domain}'

    @classmethod
    def from_url(cls, string):
        _domain = cls.is_valid_domain(string).split('//')[1]
        return cls(_domain)

    @classmethod
    def from_email(cls, string):
        _domain = cls.is_valid_domain(string)
        return cls(_domain)
''' Второй вариант решения'''    
# import re


# class DomainException(Exception):
#     pass


# class Domain:
#     __CORRECT_DOMAIN = r'\w+\.\w+'
#     __CORRECT_URL = fr'^https?://(?P<domain>{__CORRECT_DOMAIN})$'
#     __CORRECT_EMAIL = fr'\w+@(?P<domain>{__CORRECT_DOMAIN})'

#     def __init__(self, domain):
#         if not re.fullmatch(self.__CORRECT_DOMAIN, domain):
#             raise DomainException('Недопустимый домен, url или email')
#         self.domain = domain

#     def __str__(self):
#         return self.domain

#     @classmethod
#     def from_url(cls, url):
#         url = re.match(cls.__CORRECT_URL, url)
#         if not url:
#             raise DomainException('Недопустимый домен, url или email')
#         return cls(url.group('domain'))

#     @classmethod
#     def from_email(cls, email):
#         email = re.match(cls.__CORRECT_EMAIL, email)
#         if not email:
#             raise DomainException('Недопустимый домен, url или email')
#         return cls(email.group('domain'))