op = input()
cut = op.split('-')
result = 0

if cut[0] == '':
    cut = cut[1:]
    
x = sum(map(int, cut[0].split('+')))
if op[0] == '-':
    result -= x
else:
    result += x

for x in cut[1:]:
    x = sum(map(int, x.split('+')))
    result -= x

print(result)
