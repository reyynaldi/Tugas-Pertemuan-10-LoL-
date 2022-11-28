import ast
lol = ast.literal_eval(input())
b = int(input())

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
def konso_LoL(L,S):
    if kosong(S):
        return [L]
    else:
        return [L]+S


def hindar(a, L):
    if kosong(L):
        return L
    else:
        if islist(listpertama(L)):
            return konso_LoL(hindar(a, listpertama(L)),hindar(a, tail(L)))
        else:
            if listpertama(L) % a == 0: 
                return hindar(a,tail(L))
            else: 
                return konso_LoL(listpertama(L),hindar(a,tail(L)))

print(hindar(b, lol))


