from .magazyn_manager import *

def manager_create():
    manager = Manager()
    @manager.assign("zakup", 3)
    def manager_buy(manager, name, price, pieces):
        price = int(price)
        pieces = int(pieces)
        if price < 0:
            print("Błąd - cena nie może być mniejsza od zera")
            quit()
        if pieces < 0:
            print("Błąd - liczba sztuk nie może być mniejsza od zera")
            quit()
        if (price * pieces) <= manager.saldo:
            manager.lista.append("zakup")
            manager.lista.append(name)
            manager.lista.append(price)
            manager.lista.append(pieces)
            manager.magazyn[name] = manager.magazyn.get(name, 0) +pieces
            manager.saldo -= (price * pieces)
        else:
            print("Błąd - brak wystarczającej ilości środków na koncie")
            quit()
    @manager.assign("sprzedaż", 3)
    def manager_sell(manager, name, price, pieces):
        price = int(price)
        pieces = int(pieces)
        if name in manager.magazyn:
            if price < 0:
                print("Błąd - cena nie może być mniejsza od zera")
                quit()
            if pieces < 0:
                print("Błąd - liczba sztuk nie może być mniejsza od zera")
                quit()
            if (price * pieces) <= manager.saldo:
                manager.lista.append("sprzedaż")
                manager.lista.append(name)
                manager.lista.append(price)
                manager.lista.append(pieces)
                manager.magazyn[name] = manager.magazyn.get(name, 0) -pieces
                manager.saldo -= (price * pieces)
            else:
                print("Błąd - brak wystarczającej ilości środków na koncie")
                quit()
        else:
            print("Brak takiego produktu w magazynie")
            quit()
    @manager.assign("saldo", 2)
    def manager_balance(manager, money, commentary):
        manager.lista.append("saldo")
        manager.saldo += int(money)
        manager.lista.append(money)
        manager.lista.append(commentary)
    @manager.assign("konto", 0)
    def manager_review(manager):
        print("Stan konta: ", manager.saldo)
    @manager.assign("magazyn", 1)
    def manager_warehouse(manager, *any_argument):
        for arg in sys.argv[2:]:
            print(arg, manager.magazyn[arg])
    @manager.assign("przegląd", 1)
    def manager_overview(manager, *any_argument):
        saldo = 0
        lista = []
        magazyn = {}
        index = -1
        fhand = open(sys.argv[1])
        while True:
            y = int(sys.argv[2])
            z = int(sys.argv[3])
            fh = fhand.readline().strip()
            if fh.startswith("saldo"):
                money = fhand.readline().strip()
                com = fhand.readline().strip()
                saldo += int(money)
                index += 1
                if index >= y and index <= z:
                    lista.append(fh)
                    lista.append(money)
                    lista.append(com)
                continue
            if fh.startswith("zakup"):
                name = fhand.readline().strip()
                price = int(fhand.readline().strip())
                if price < 0:
                    print("Błąd - cena nie może być mniejsza od zera")
                    quit()
                pieces = int(fhand.readline().strip())
                if pieces < 0:
                    print("Błąd - liczba sztuk nie może być mniejsza od zera")
                    quit()
                if (price * pieces) <= saldo:
                    magazyn[name] = magazyn.get(name, 0) +pieces
                    saldo -= (price * pieces)
                    index += 1
                    if index >= y and index <= z:
                        lista.append(fh)
                        lista.append(name)
                        lista.append(price)
                        lista.append(pieces)
                    continue
                else:
                    print("Błąd - brak wystarczającej ilości środków na koncie")
                    quit()
            if fh.startswith("sprzedaż"):
                name = fhand.readline().strip()
                if name in magazyn:
                    price = int(fhand.readline().strip())
                    if price < 0:
                        print("Błąd - cena nie może być mniejsza od zera")
                        quit()
                    pieces = int(fhand.readline().strip())
                    if pieces < 0:
                        print("Błąd - liczba sztuk nie może być mniejsza od zera")
                        quit()
                    if (price * pieces) <= saldo:
                        magazyn[name] = magazyn.get(name, 0) -pieces
                        saldo -= (price * pieces)
                        index += 1
                        if index >= y and index <= z:
                            lista.append(fh)
                            lista.append(name)
                            lista.append(price)
                            lista.append(pieces)
                        continue
                    else:
                        print("Błąd - brak wystarczającej ilości środków na koncie")
                        quit()
                else:
                    print("Brak takiego produktu w magazynie")
                    quit()
            if fh.startswith(""):
                break
        for element in lista:
            print(element)
    return manager
