print('''
    Программа для подсчёта количества подсыпки.
===================================================================
Коэфициент уплотнения(1.12) и вес подсыпаемого материала (1500кг/куб)
По умолчанию установлены для строительного песка.
Что бы изменить, вводите новые значения когда запросит программа.
===================================================================
    ''')
input('Нажмите <Enter> для продолжения...\n\n')

class Osnova():
    def __init__(self, dl=None, sh=None, vis=None, upl=1.12):
        self.dl = dl
        self.sh = sh
        self.vis = vis
        self.ves = 1500
        self.upl = upl
    def plosh(self):
        return self.dl * self.sh
    def kubov(self):
        return self.plosh() * self.vis
    def massa(self):
        return self.kubov() * self.ves * self.upl
ps = Osnova()

for x in ps.__dict__.keys():
    try:
        if x == 'dl':
            ps.dl = float(input("Введите измеряемую длинну: "))
        if x == 'sh':
            ps.sh = float(input("Введите измеряемую ширину: "))
        if x == 'vis':
            ps.vis = float(input("Введите толщину подсыпки: "))
        if x == 'upl':
            try:
                print("\nИзменить вес материала в одном кубе?")
                vopr = float(input("Для подсчёта без изменений нажмите <Enter>: "))
                ps.ves = vopr
            except:
                pass
                
            try:
                print("\nКоэфициент уплотнения - 1.12\nВведите своё значение, или нажмите <Enter> что бы пропустить. ")
                vopr = float(input("Для подсчёта без учёта коэфициента, введите '1': "))
                ps.upl = vopr
            except:
                pass
    except:
        input('\n# Ошибка\n# Поля "Длинна, ширина и толщина" не могут быть пустыми, или иметь отрицательные значения')
        import sys
        sys.exit()

rnd = round(ps.massa())
masspr = '{:,}'.format(rnd)
if len(masspr) >= 5:
    masspr = masspr[:masspr.find(',')+2]
elif len(masspr) == 3:
    masspr = '0.' + masspr[:masspr.find(',')+2]
else:
    masspr = '-'

ploshpr = '\n* Площадь - {:.1f} квадрат(ов)'.format(ps.plosh())
kubovpr = '* Объем - {:.1f} куб(ов)'.format(ps.kubov())

print(ploshpr.replace('.', ','))
print(kubovpr.replace('.', ','))
print('* Масса - {} тонн ({:.0f}кг)'.format(masspr, ps.massa()))

print('\n=============================================================\n')

input("<Enter> для выхода...\n")
