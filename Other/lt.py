import random


def rmz(cntr):
    result = '*' * (cntr*2+1)
    rnd = random.choice(range(len(result)))
    nwstr = result[:rnd] + 'o' + result[rnd+1:]
    return nwstr

x = int(input('Введите высоту ёлочки 2<n<20: '))

for k in range(x):
    if x<2 or x>20:
        print('Неправильное значение :(')
        break
    if not k % 2 == 0:
        print('%s%s%s' %('_'*(x-k-1), rmz(k), '_'*(x-k-1)))
    else:
        print('%s%s%s' %('_'*(x-k-1), '*'*(k*2+1), '_'*(x-k-1)))


p = input()

