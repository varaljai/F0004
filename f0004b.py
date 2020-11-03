név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ')

kor = int(kor) 
év = input('Melyik évben járunk? ')
év = int(év)

születési_év = év - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')

érettségi_év = (születési_év + 18)
print(név, ', kend ', érettségi_év, '-ban érettségizik.', sep='') 