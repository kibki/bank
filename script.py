per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите сумму вклада (рублей): '))
TKB=int(per_cent['ТКБ']*money)
SKB=int(per_cent['СКБ']*money)
VTB=int(per_cent['ВТБ']*money)
SBER=int(per_cent['СБЕР']*money)
deposit=[TKB, SKB, VTB, SBER]
print("deposit =",deposit)
i=max(deposit)
print("Максимальная сумма, которую Вы можете заработать - ", i)

