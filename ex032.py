import datetime
year = int(input('Digite um ano para ser avaliado: '))
leap_year = year % 4
if leap_year == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é bissexto.'.format(year))
else:
    print('O ano {} não é bissexto.'.format(year))
