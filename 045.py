from random import choice
from time import sleep

print('*'*35)
print('\033[31m|{:^28} |\033[m'.format('👊🖐 ✌ Vamos jogar Jokenpô? 👊🖐 ✌'))
print('*'*35)

elmnt = ['pedra👊', 'papel🖐', 'tesoura✌']
pc = choice(elmnt)
print('\033[33mPedra👊\033[m')
sleep(0.5)
print('\033[34mPapel🖐\033[m')
sleep(0.5)
print('\033[31mTesoura✌\033[m')
sleep(0.5)
ad = str(input('Qual a sua escolha: ')).lower().strip()

if ad == 'pedra':
    ad = 'pedra👊'
elif ad == 'papel':
    ad = 'papel🖐'
elif ad == 'tesoura':
    ad = 'tesoura✌'
else:
    ad = 'inválido'
print('\033[33mJO')
sleep(0.8)
print('\033[33mKEN\033[m')
sleep(0.8)
print('\033[33mPÔ\033[m')
sleep(0.5)
if pc == ad:
    print('\033[35mEMPATE!\033[m')
    print(f'Tanto o computador quanto você jogaram {pc}.')
elif pc == 'pedra👊' and ad == 'tesoura✌' or pc == 'tesoura✌' and ad == 'papel🖐' or pc == 'papel🖐' and ad == 'pedra👊':
    print('\033[31mO COMPUTADOR VENCEU!!\033[m')
    print(f'O computador colocu {pc}  e você colocou {ad} .')
elif ad == 'inválido':
    print('Poxa vida, você escolheu uma opção inválida! Vamos tentar novamente?')
else:
    print('VOCÊ VENCEU!!')
    print(f'Eu coloquei {pc} e você {ad} .')
