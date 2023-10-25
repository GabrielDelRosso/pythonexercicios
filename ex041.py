import time
year = int(input('Digite o ano que o atleta nasceu: '))
print('O atleta nasceu em {}.'.format(year))
actual_year = time.localtime()
print('O ano da competição atual é {}.'.format(actual_year[0]))
athlete_age = actual_year[0] - year
print('A idade atual do atleta é {} anos.'.format(athlete_age))
if athlete_age <= 9:
    print('O atleta faz parte da categoria MIRIM!')
elif athlete_age <= 14:
    print('O atleta faz parte da categoria INFANTIL!')
elif athlete_age <= 19:
    print('O atleta faz parte da categoria JÚNIOR!')
elif athlete_age <= 25:
    print('O atleta faz parte da categoria SÊNIOR')
else:
    print('O atleta faz parte da categoria MASTER!')
