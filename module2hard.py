import random
def cipher():
    num=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    numbers = list(range(3,21))
    cipher = random.choice(numbers)
    return cipher
def passcode(n):
    passdict = {}
    passdict.update({3:12, 4:13,5:1423, 6:121524, 7:162534})
    passdict.update({8:13172635, 9:1218273645, 10:141923283746})
    passdict.update({11:11029384756, 12:12131511124210394857, 13:112211310495867})
    passdict.update({13:1611325212343114105968, 14:1214114232133124115106978, 15:1214114232133124115106978})
    passdict.update({16:1317115262143531341251161079, 17:11621531441351261171089, 18:12151811724272163631545414513612711810})
    passdict.update({19:118217316415514613712811910, 20:13141911923282183731746416515614713812911})
    passcode = passdict.get(n)
    return passcode

n = cipher()
print('Шифр   :', n)
a1 = list(range(1, n))
a2 = list(range(1, n))
pairs = []
result = ''
for i  in a1:
    for j in a2:
        pairnum1 = i
        pairnum2 = j
        if pairnum1 >= pairnum2:
            continue
        else:
            dell = n%(pairnum1+pairnum2)
            if dell == 0:
                pairs.append([pairnum1, pairnum2])
                result =  result + str(pairnum1) + str(pairnum2)
print('Пары чисел', *pairs)
print('Введите пароль', result, 'во вторую вставку')
if int(result) == passcode(n):
    print('Проходите')





