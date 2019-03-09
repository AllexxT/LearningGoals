_list = [chr(x) for x in range(65, 91)]
nwl = []
for x in _list:
    for y in _list:
        nwl.append(x+y)
_list += nwl
_list.insert(0, None)
_dict = dict(zip(range(len(_list)+1), _list))           #1-702
_list.pop(0)
dict2 = dict(zip(range(703, 703 + len(_list)), _list))  #703-1404


class Engine:
    def __init__(self):
        self.diap1 = _dict
        self.diap2 = dict2
    def __call__(self, value):
        if value == 0:
            print('!Range is 1 - 1404')
            pass
        elif value <= 702:
            print('String #1 =>', self.diap1[value])
        elif 702 < value <= 1404:
            print('String #2 =>', self.diap2[value])
        else:
            print('!Range is 1 - 1404')

# For console testing
test = Engine()
while True:
    try:
        test(int(input("Enter value: ")))
        print()
    except:
        break
    
    
