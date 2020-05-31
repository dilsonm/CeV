import urllib.request

try:
    urllib.request.urlopen('http://www.pudin.com.br')
except:
    print('Deu erro.')
else:
    print('Tudo ok')

