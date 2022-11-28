import ast
list_of_list = ast.literal_eval(input())

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

def jmlhkartu(L):
  if kosong(L):
    return 0
  else:
    if atom(listpertama(L)): 
      print(L, "1")
      return jmlhkartu(tail(L)) + 1
    else: 
      if atom(L): 
        print(L, "2")
        return jmlhkartu(listpertama(L)) 
      else:
        print(L, "3")
        return jmlhkartu(listpertama(L)) + jmlhkartu(tail(L)) 



print(jmlhkartu(list_of_list))
