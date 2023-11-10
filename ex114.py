import requests

try:
    site = input('Insira o link: ')
    check = requests.get(site)
except:
    print('Site offline.')
else:
    print('Site acessível.')
