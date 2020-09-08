# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class Equipment:
    eqmt_type = None

    def __init__(self, manufacture='', model=''):
        self._manufacture = manufacture
        self._model = model

    def __str__(self):
        return f'eqmt_type: {self.eqmt_type}, manufacturer: {self._manufacture}, model: {self._model}'

    # @property
    # def eqmt_type(self):
    #     return self._eqmt_type

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, val):
        self._model = val

    @property
    def manufacture(self):
        return self._manufacture

    @manufacture.setter
    def manufacture(self, val):
        self._manufacture = val


class Printer(Equipment):
    eqmt_type = 'printer'


class Scanner(Equipment):
    eqmt_type = 'scanner'


class Xerox(Equipment):
    eqmt_type = 'xerox'


class Storage:
    def __init__(self):
        self._equipments = {}

    def add(self, eqmt):
        new_dict = {eqmt.eqmt_type: {'manufacture': eqmt.manufacture, 'model': eqmt.model, 'location': 'Storage'}}
        if eqmt.eqmt_type not in self._equipments.keys():
            self._equipments[eqmt.eqmt_type] = [new_dict[eqmt.eqmt_type]]
        else:
            self._equipments[eqmt.eqmt_type].append(new_dict[eqmt.eqmt_type])

    def get_eqmt_type_list(self):
        return list(self._equipments.keys())

    def get_eqmt_count(self, eqmt_type):
        tmp_list = self._equipments.get(eqmt_type)
        if tmp_list != None:
            return len(tmp_list)
        else:
            return 0

    def move_equipment(self, eqmt_type='', manufacture='', model='', new_location='', old_location=''):
        if old_location == '':
            old_location = 'Storage'
        if self._equipments.get(eqmt_type) != None and new_location != old_location:
            for el in self._equipments.get(eqmt_type):
                if el['manufacture'] == manufacture and el['model'] == model and el['location'] == old_location:
                    el['location'] = new_location
            return True
        else:
            return False

    def get_equipments(self, eqmt_type=''):
        tmp_list = self._equipments.get(eqmt_type)
        if tmp_list != None:
            return tmp_list
        else:
            return 0

    def del_equipment(self, eqmt_type='', manufacture='', model='', location=''):
        if location == '':
            location = 'Storage'
        if self.get_equipments(eqmt_type) == 0:
            self._equipments.pop(eqmt_type)
            return True
        else:
            if self._equipments.get(eqmt_type) != None:
                for el in self._equipments.get(eqmt_type):
                    if el['manufacture'] == manufacture and el['model'] == model and el['location'] == location:
                        self._equipments[eqmt_type].remove(el)
                        break
                return True
            else:
                return False


storage_1 = Storage()

printers = [{"manufacturer": "Cannon", "model": "LBP6000"},
            {"manufacturer": "HP", "model": "Laserjet 1120"},
            {"manufacturer": "Epson", "model": "XP-3100"},
            {"manufacturer": "HP", "model": "LaserJet 1180"}, ]

scaners = [{"manufacturer": "Cannon", "model": "Canoscan Lide_100"},
           {"manufacturer": "Epson", "model": "V370"},
           {"manufacturer": "Epson", "model": "V350"},
           {"manufacturer": "HP", "model": "PerfectScan 400"}]

xerox = [{"manufacturer": "Xerox", "model": "xr2000"},
         {"manufacturer": "HP", "model": "x500"},
         {"manufacturer": "Xerox", "model": "xr2000"},
         {"manufacturer": "Xerox", "model": "xr2000"}, ]

printer_list = list(map(lambda x: Printer(x['manufacturer'], x['model']), printers))
scaner_list = list(map(lambda x: Scanner(x['manufacturer'], x['model']), scaners))
xerox_list = list(map(lambda x: Xerox(x['manufacturer'], x['model']), xerox))

# добавляем объекты на склад.
storage_1.add(printer_list[0])
storage_1.add(printer_list[1])
storage_1.add(scaner_list[0])
storage_1.add(xerox_list[1])

print(storage_1.get_eqmt_type_list())
print(f" Количество принтеров на складе: {storage_1.get_eqmt_count('printer')}")
# перемещение оборудования в другой отдел.
print(storage_1.get_equipments('printer'))
print(f"перемещение оборудования: {storage_1.move_equipment('printer', 'Cannon', 'LBP6000', 'dept_of_sicrets')}")
print(storage_1.get_equipments('printer'))

print(f"списание оборудования: {storage_1.del_equipment('printer', 'Cannon', 'LBP6000', 'dept_of_sicrets')}")
print(storage_1.get_equipments('printer'))
