"""cidade = str(input('Em que cidade você nasceu?: ')).upper()
santo = cidade.split()
if santo[0] == 'SANTO':
    print('Ok, essa cidade começa com Santo')
else:
    print('Essa cidade não começa com Santo.')"""

cid = str(input('Em que cidade você nasceu?: ')).upper()
print(cid[0:5] == 'SANTO')
