import ast

def kosong(a):
    return a == []
def tail(a):
    if not(kosong(a)):
        return a[1:]
def listpertama(a):
    return a[0]
def atom(a):
    return not(kosong(a)) and jumlah(a) == 1
def islist(a):
    return not(atom(a))
def jumlah(a):
    if kosong(a):
        return 0
    else:
        try:
            return 1+jumlah(tail(a))
        except TypeError:
            return 1
def islist(L):
    if type(L) == list or not(atom(L)):
        return True
    else:
        return False
def isganjil(L):
         return int(L) == 1 or int(L)%2 == 1
def isgenap(L):
    return int(L) == 2 or int(L)%2 == 0

def hitungisi(L):
    return sum(L)


def jml_elemen_lol(L):
    if kosong(L):
        return 0
    else:
        if atom(listpertama(L)):
            print(L, "1")
            if isgenap(listpertama(L)):
                return listpertama(L)*4000+jml_elemen_lol(tail(L))
            elif isganjil(listpertama(L)):
                return listpertama(L)*3000+jml_elemen_lol(tail(L))
            else:
                return "Ngaco"
        else:
            print(L, "3")
            if atom(L):
                return jml_elemen_lol(listpertama(L))
            else:
                print(L, "A")
                print(islist(L))
                if isgenap(hitungisi(listpertama(L))):
                    return hitungisi(listpertama(L))*2000+jml_elemen_lol(tail(L))
                else:
                    return hitungisi(listpertama(L))*1000+jml_elemen_lol(tail(L))



list_of_list = ast.literal_eval(input())
print((jml_elemen_lol(list_of_list)))