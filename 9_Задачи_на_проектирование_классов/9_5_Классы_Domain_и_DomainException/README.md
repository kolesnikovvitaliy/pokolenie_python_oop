<h2 style="text-align:center">Классы Domain и DomainException</h2>

### Реализуйте класс исключений DomainException. Также реализуйте класс Domain для работы с доменами. Класс Domain должен поддерживать три способа создания своего экземпляра: напрямую через вызов класса, а также с помощью двух методов класса from_url() и from_email():
```python
domain1 = Domain('pygen.ru')                       # непосредственно на основе домена
domain2 = Domain.from_url('https://pygen.ru')      # на основе url-адреса
domain3 = Domain.from_email('support@pygen.ru')    # на основе адреса электронной почты
```
#### При попытке создания экземпляра класса Domain на основе некорректных домена, url-адреса или адреса электронной почты должно быть возбуждено исключение DomainException с текстом:

> Недопустимый домен, url или email
#### В качестве неформального строкового представления экземпляр класса Domain должен иметь собственный домен:
```python
print(str(domain1))                                # pygen.ru
print(str(domain2))                                # pygen.ru
print(str(domain3))                                # pygen.ru
```
#### Примечание 1. Будем считать домен корректным, если он представляет собой последовательность из одной или более латинских букв, за которой следует точка, а затем снова одна или более латинских букв.

#### Примечание 2. Будем считать url-адрес корректным, если он представляет собой строку http:// или https://, за которой следует корректный домен. 

#### Примечание 3. Будем считать адрес электронной почты корректным, если он представляет собой последовательность из одной или более латинских букв, за которой следует собачка (@), а затем корректный домен.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">domain1 = Domain('pygen.ru')<br>
                        domain2 = Domain.from_url('https://pygen.ru')<br>
                        domain3 = Domain.from_email('support@pygen.ru')<br>
                        print(domain1)<br>
                        print(domain2)<br>
                        print(domain3)<br></td>
      <td align="center">try:<br>
                            domain1 = Domain('pygen..org')<br>
                        except DomainException as e:<br>
                            print(e)<br></td>
      <td align="center">domain1 = Domain('stepik.org')<br>
                          domain2 = Domain.from_url('https://stepik.org')<br>
                          domain3 = Domain.from_email('support@stepik.org')<br>
                          print(domain1)<br>
                          print(domain2)<br>
                          print(domain3)<br></td>
      <td align="center">domains = ['ip.ru', 'ao.org', 'npo.com', 'npo.com', 'zao.org', 'sibtred.info', 'ao.biz', 'npo.net', 'npo.net', 'oao.net', 'zao.com', 'pahomov.org', 'bikova.ru', 'ooo.ru', 'transol.net', 'zao.com', 'rao.info', 'ooo.org','krjukov.com', 'nikonova.com']<br>
                      for d in domains:<br>
                          domain = Domain(d)<br>
                          print(domain)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        pygen.ru<br>
                        pygen.ru<br>
                        pygen.ru<br>
      </td>
      <td align="center">
                        Недопустимый домен, url или email<br>
      </td>
      <td align="center">
                        stepik.org<br>
                        stepik.org<br>
                        stepik.org<br>
      </td>
      <td align="center">
                        ip.ru<br>
                        ao.org<br>
                        npo.com<br>
                        npo.com<br>
                        zao.org<br>
                        sibtred.info<br>
                        ao.biz<br>
                        npo.net<br>
                        npo.net<br>
                        oao.net<br>
                        zao.com<br>
                        pahomov.org<br>
                        bikova.ru<br>
                        ooo.ru<br>
                        transol.net<br>
                        zao.com<br>
                        rao.info<br>
                        ooo.org<br>
                        krjukov.com<br>
                        nikonova.com<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
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
```
* Второй вариант решения

```python
import re


class DomainException(Exception):
    pass


class Domain:
    __CORRECT_DOMAIN = r'\w+\.\w+'
    __CORRECT_URL = fr'^https?://(?P<domain>{__CORRECT_DOMAIN})$'
    __CORRECT_EMAIL = fr'\w+@(?P<domain>{__CORRECT_DOMAIN})'

    def __init__(self, domain):
        if not re.fullmatch(self.__CORRECT_DOMAIN, domain):
            raise DomainException('Недопустимый домен, url или email')
        self.domain = domain

    def __str__(self):
        return self.domain

    @classmethod
    def from_url(cls, url):
        url = re.match(cls.__CORRECT_URL, url)
        if not url:
            raise DomainException('Недопустимый домен, url или email')
        return cls(url.group('domain'))

    @classmethod
    def from_email(cls, email):
        email = re.match(cls.__CORRECT_EMAIL, email)
        if not email:
            raise DomainException('Недопустимый домен, url или email')
        return cls(email.group('domain'))
```


