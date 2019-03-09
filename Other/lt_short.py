import random
def rmz(cntr):
    result = '*' * (cntr*2+1)
    rnd = random.choice(range(len(result)))
    return result[:rnd] + 'o' + result[rnd+1:]
n = int(input('Введите высоту ёлочки: '))
[print('_'*(n-i-1) + rmz(i) + '_'*(n-i-1)) if i%2!=0 else print('_'*(n-i-1) + '*'*(i*2+1) + '_'*(n-i-1)) for i in range(n) if 2<n<20]
input()
