'''
Принципы римской системы счисления
В настоящее время в римской системе счисления используются следующие знаки:

I = 1; V = 5; X = 10; L = 50; C = 100; D = 500; M = 1000.
Все целые числа от 1 до 3999 записываются с помощью приведенных выше цифр.
При этом:
* если большая цифра стоит перед меньшей, они складываются:
VI = 5 + 1 = 6; XV = 10 + 5 = 15; LX = 50 + 10 = 60; CL = 100 + 50 = 150;

* если меньшая цифра стоит перед большей (в этом случае она не может повторяться),
то меньшая вычитается из большей; вычитаться могут только цифры, обозначающие 1 или степени 10;
уменьшаемым может быть только цифра, ближайшая в числовом ряду к вычитаемой:
IV = 5 - 1 = 4; IX = 10 - 1 = 9; XL = 50 - 10 = 40; XC = 100 - 10 = 90;

* цифры V, L, D не могут повторяться; цифры I, X, C, M могут повторяться не более трех раз подряд:
VIII = 8; LXXX = 80; DCCC = 800; MMMD = 3500.
'''
class Stack:
    def __init__(self):
        self.items = []
        self.counter = 0
    def isEmpty(self):
        return self.items == []
    def __iter__(self):
        return self
    def __next__(self):
        self.limit = len(self.items)
        if self.counter < self.limit:
            self.counter += 1
            return self.items[self.counter - 1]
        else:
            self.counter = 0
            raise StopIteration
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def __repr__(self):
        return str(self.items)

# Конвертирует римские цифры в арабские
# Используется стек(код выше)
def toArabic(number):
    stack = Stack()
    roma = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    temp = ' '.join(number).split()
    for x in range(len(number)):
        if number[x] not in roma:
            return print('Wrong numeral')
    for num in temp:
        if not stack.isEmpty() and roma[num] > stack.peek():
            tmp = roma[num] - stack.peek()
            stack.pop()
            stack.push(tmp)
            continue
        stack.push(roma[num])
    result = sum(stack)
    return result


# Разделяет число на слагаемые
# Прим.: 246 == [200, 40, 6]
def splitToAdditions(number):
    adt = []
    num = str(number)
    for x in range(len(str(number))):
        tmp = int(str(num)[:1]+'0'*(len(str(num))-1))
        if tmp > 0:
            adt.append(tmp)
        tm = ' '.join(num).split()
        tm.pop(0)
        num = ''.join(tm)
    return adt

# Обрезает число возвращая первую цифру слева, если она <= 3
# Прим.: 240 == 2, 350 == 3, 450 == None
def tailCut(numb):
    tmp = int(str(numb)[:1])
    if tmp == 4:
        return 4
    elif tmp > 3:
        return None
    return tmp

# Выбирает римскую букву для арабской цифры
def chooseLetter(number=200):
    top = [6, 7, 8, 60, 70, 80, 600, 700, 800]
    roma = 'Nan'
    tC = tailCut(number)
    if number in list(range(1,4)):
        roma = 'I'
    elif number in [10,20,30]:
        roma = 'X'
    elif number in [100,200,300]:
        roma = 'C'
    elif number in [1000,2000,3000]:
        roma = 'M'
    elif number == 4:
        return 'IV'
    elif number == 40:
        return 'XL'
    elif number == 9:
        return 'IX'
    elif number == 90:
        return 'XC'
    elif number == 900:
        return 'CM'
    elif number == 400:
        return 'CD'
    elif number in [5]:
        return  'V'
    elif number in [50]:
        return  'L'
    elif number in [500]:
        return  'D'
    elif number in top:
        for x in top:
            if number % 5 != 0:
                incr = chooseLetter(number % 5)
                tm = ''
                for x in incr:
                    tm += x
                return 'V' + tm
            elif number % 50 != 0:
                incr = chooseLetter(number % 50)
                tm = ''
                for x in incr:
                    tm += x
                return 'L' + tm
            elif number % 500 != 0:
                incr = chooseLetter(number % 500)
                tm = ''
                for x in incr:
                    tm += x
                return 'D' + tm
    return [roma for x in range(tC)]


def toRoma(num):
    roma = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    split = splitToAdditions(num)
    res = ''
    for x in split:
        for y in chooseLetter(x):
            res += y
    return res


def convert(num):
    if type(num) == str:
        return toArabic(num)
    else:
        return toRoma(num)





if __name__ == '__main__':
    
    def tests():
        rm = ['X', 'L', 'C', 'D', 'M']
        arab = [10, 50, 100, 500, 1000]
        print('Testing roma to arabic numbers convertation')
        for x in range(len(rm)):
            assert convert(rm[x]) == arab[x], 'Test №%d is FAILED!' % x
            print('{} -> {}'.format(rm[x], arab[x]))
            print('test %s is passed' % str(x+1))
        print('Testing arabic to roma numbers convertation')
        for x in range(len(rm)):
            assert convert(arab[x]) == rm[x], 'Test №%d is FAILED!' % x
            print('{} -> {}'.format(arab[x], rm[x]))
            print('test %s is passed' % str(x+1))
        
        print('All tests is passed!')
