import sys, os


class Manager():
    """Warehouse management system"""

    def __init__(self):
        self.saldo = 0
        self.lista = []
        self.magazyn = {}
        self.actions = {}
        self.manager_sell = None
        self.manager_buy = None
        self.manager_balance = None
        self.manager_review = None
        self.manager_warehouse = None
        self.manager_overview = None

    def file_read(self, fhand):
        fhand = open(fhand)
        while True:
            fh = fhand.readline().strip()
            if fh == "":
                return (self.saldo, self.lista, self.magazyn)
            args = [fhand.readline().strip() for i in range(self.actions[fh][1])]
            self.actions[fh][0](self, *args)

    def argv_read(self):
        fh = sys.argv[0]
        path = os.path.splitext(fh)
        filename = path[-2]
        args = sys.argv[2:]
        self.actions[filename][0](self, *args)
        return (self.saldo, self.lista, self.magazyn)

    def file_write(self, fname):
        fd = open(fname, "w")
        for element in self.lista:
            fd.write(str(element))
            fd.write("\n")

    def assign(self, name, qty):
        def decorator(cb):
            self.actions[name] = (cb, qty)
        return decorator

'''
from manager.models (lub .models?) import Goods
for x in range (len)self.manazyn in self.manazyn:
    g = Goods(name=#klucz slownika, qty=#wartosc slownika)
    g.save()

a prpstsza wersja bez bazy spropbowac z views wywowywac akcje jak tutraj i
zapisanie do pliku intxt
'''
