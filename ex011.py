paredelar = float(input('Qual a largura da parede que deve ser pintada? '))
paredealt = float(input('Qual a altura da parede que deve ser pintada? '))
paredearea = paredelar * paredealt
paredetinta = paredearea/2
print('=====')
print('A largura da parede é {}, a altura é {}, a área da parede é {}m², sendo necessários {}l de tinta para sua pintura.'.format(paredelar, paredealt, paredearea, paredetinta))
print('=====')
