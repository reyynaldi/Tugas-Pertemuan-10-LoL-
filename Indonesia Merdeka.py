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
def hitungisi(L):
    return sum(L)    
def tertinggi(L):
    if kosong(L):
        return 0
    elif atom(L):
        return L
    else:
        try:
            return max(list(set(L)))
        except TypeError:
            return listpertama(L)

def kaliseribu(a):
    return a*1000000

def ninja(L):
    if kosong(L):
        return 0
    elif atom(listpertama(L)):
        if islist(listpertama(L)):
            return ninja(listpertama(L))+ninja(tail(L))
        else:
            return (listpertama(L)*1000000)+ninja(tail(L))
    else:
        if atom(L):
            return tertinggi(listpertama(L))*1000000
        else:
            return kaliseribu(tertinggi(listpertama(L)))+ninja(tail(L))


list_of_list = ast.literal_eval(input())
print(ninja(list_of_list))


