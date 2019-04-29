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

def toRoma(number):
    roma = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    adt = []
    num = str(number)
    for x in range(len(str(number))):
        tmp = int(str(num)[:1]+'0'*(len(str(num))-1))
        if tmp > 0:
            adt.append(tmp)
        tm = ' '.join(num).split()
        tm.pop(0)
        num = ''.join(tm)
    print(adt)


#one = int(str(x)[:1]+'0'*(len(str(x))-1))



if __name__ == '__main__':
    
    def tests():
        rm = ['X', 'L', 'C', 'D', 'M']
        arab = [10, 50, 100, 500, 1000]
        for x in range(len(rm)):
            assert toArabic(rm[x]) == arab[x], 'Test №%d is FAILED!' % x
            print('test %s is passed' % str(x+1))
        print('All tests is passed!')
